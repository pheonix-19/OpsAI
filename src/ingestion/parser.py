# src/ingestion/parser.py
import csv
import json
import os
from typing import List, Dict, Any

def load_csv(path: str) -> List[Dict[str, Any]]:
    tickets = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tickets.append({
                'title':      row.get('Subject', '').strip(),
                'body':       row.get('Description', '').strip(),
                'labels':     [l.strip() for l in row.get('Tags', '').split(',') if l.strip()],
                'resolution': row.get('Resolution', '').strip(),
            })
    return tickets

def load_json(path: str) -> List[Dict[str, Any]]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # expect either {"tickets": [...]} or a raw list
    return data.get('tickets', data if isinstance(data, list) else [])

def normalize_ticket(ticket: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'title':      ticket.get('title', '').strip(),
        'body':       ticket.get('body', '').strip(),
        'labels':     ticket.get('labels', []),
        'resolution': ticket.get('resolution', '').strip(),
    }

def save_processed(tickets: List[Dict[str, Any]], output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)
    for i, t in enumerate(tickets):
        fn = os.path.join(output_dir, f'ticket_{i}.json')
        with open(fn, 'w', encoding='utf-8') as f:
            json.dump(t, f, ensure_ascii=False, indent=2)
