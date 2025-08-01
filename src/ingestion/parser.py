#!/usr/bin/env python3
"""
OpsAI Data Parser

Author: Ayush
GitHub: https://github.com/pheonix-19
Project: OpsAI - Intelligent IT Support Automation
Copyright (c) 2025 Ayush. All rights reserved.

This module handles parsing of various data formats for ticket ingestion.
"""

import csv
import json
import os
from typing import List, Dict, Any

def load_csv(path: str) -> List[Dict[str, Any]]:
    """
    Load tickets from a CSV file.
    Expects columns: Subject, Description, Tags, Resolution.
    """
    tickets: List[Dict[str, Any]] = []
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
    """
    Load tickets from a JSON file.
    - If JSON is a dict with key 'tickets', returns data['tickets'].
    - If JSON is a list, returns it directly.
    - Otherwise returns [].
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, dict):
        return data.get('tickets', [])
    elif isinstance(data, list):
        return data
    else:
        return []

def normalize_ticket(ticket: Dict[str, Any]) -> Dict[str, Any]:
    """
    Ensure each ticket has clean 'title', 'body', 'labels', and 'resolution' fields.
    """
    return {
        'title':      ticket.get('title', '').strip(),
        'body':       ticket.get('body', '').strip(),
        'labels':     ticket.get('labels', []) if isinstance(ticket.get('labels', []), list) else [],
        'resolution': ticket.get('resolution', '').strip(),
    }

def save_processed(tickets: List[Dict[str, Any]], output_dir: str) -> None:
    """
    Write each normalized ticket to its own JSON file under output_dir.
    """
    os.makedirs(output_dir, exist_ok=True)
    for idx, ticket in enumerate(tickets):
        filename = os.path.join(output_dir, f'ticket_{idx}.json')
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(ticket, f, ensure_ascii=False, indent=2)
