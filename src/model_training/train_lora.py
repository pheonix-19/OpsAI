# src/model_training/train_lora.py

import os
import json
import argparse
import torch
from torch.utils.data import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
    BitsAndBytesConfig,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

class TicketDataset(Dataset):
    def __init__(self, data_dir: str, tokenizer, max_length: int = 512):
        self.samples = []
        self.tokenizer = tokenizer
        self.max_length = max_length

        # load all tickets
        files = sorted(f for f in os.listdir(data_dir) if f.endswith('.json'))
        for fn in files:
            ticket = json.load(open(os.path.join(data_dir, fn), 'r', encoding='utf-8'))
            prompt = f"Ticket: {ticket['title']} {ticket['body']}\nSolution:"
            target = ticket.get('resolution', '')
            self.samples.append((prompt, target))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        prompt, target = self.samples[idx]
        # build input+label text
        full = prompt + " " + target
        enc = self.tokenizer(
            full,
            truncation=True,
            max_length=self.max_length,
            padding='max_length',
        )
        input_ids = torch.tensor(enc.input_ids)
        attention_mask = torch.tensor(enc.attention_mask)
        # labels: mask prompt tokens
        labels = input_ids.clone()
        prompt_len = len(self.tokenizer(prompt, add_special_tokens=False).input_ids)
        labels[:prompt_len] = -100
        return {
            'input_ids':        input_ids,
            'attention_mask':   attention_mask,
            'labels':           labels,
        }

def main():
    parser = argparse.ArgumentParser(description="Fine‑tune LLM on ticket data with LoRA/QLoRA")
    parser.add_argument('--data-dir',     required=True,  help="Processed tickets JSON dir")
    parser.add_argument('--output-dir',   required=True,  help="Where to save fine‑tuned adapter")
    parser.add_argument('--base-model',   required=True,  help="HuggingFace model ID (e.g. Mistral‑7B‑instruct)")
    parser.add_argument('--epochs',       type=int, default=3)
    parser.add_argument('--batch-size',   type=int, default=4)
    parser.add_argument('--max-length',   type=int, default=512)
    parser.add_argument('--learning-rate',type=float, default=3e-4)
    args = parser.parse_args()

    # tokenizer + model with 4‑bit quantization
    tokenizer = AutoTokenizer.from_pretrained(args.base_model, use_fast=True)
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type='nf4',
        bnb_4bit_compute_dtype=torch.float16,
    )
    model = AutoModelForCausalLM.from_pretrained(
        args.base_model,
        quantization_config=bnb_config,
        device_map='auto',
    )
    model = prepare_model_for_kbit_training(model)

    # attach LoRA
    lora_cfg = LoraConfig(
        r=8,
        lora_alpha=32,
        target_modules=['q_proj','k_proj','v_proj','o_proj'],
        lora_dropout=0.05,
        bias='none',
        task_type='CAUSAL_LM',
    )
    model = get_peft_model(model, lora_cfg)

    # dataset & training
    dataset = TicketDataset(args.data_dir, tokenizer, max_length=args.max_length)
    training_args = TrainingArguments(
        output_dir=args.output_dir,
        per_device_train_batch_size=args.batch_size,
        num_train_epochs=args.epochs,
        learning_rate=args.learning_rate,
        logging_steps=10,
        save_total_limit=2,
        fp16=True,
        remove_unused_columns=False,
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        tokenizer=tokenizer,
    )

    trainer.train()
    # save only the adapter weights
    model.save_pretrained(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    print(f"[✅] LoRA adapter saved to {args.output_dir}")

if __name__ == '__main__':
    main()
