#!/usr/bin/env python3
"""
Ingestion Module
Reads raw tickets and processes them into normalized JSON files.
"""

import os
import sys
import glob

try:
    from .parser import load_csv, load_json, normalize_ticket, save_processed
except ImportError:
    # For direct execution
    sys.path.append(os.path.dirname(__file__))
    from parser import load_csv, load_json, normalize_ticket, save_processed


def main(raw_dir: str, out_dir: str):
    tickets = []
    # load all CSVs
    for path in glob.glob(f'{raw_dir}/*.csv'):
        tickets.extend(load_csv(path))
    # load all JSONs
    for path in glob.glob(f'{raw_dir}/*.json'):
        tickets.extend(load_json(path))

    processed = [normalize_ticket(t) for t in tickets]
    save_processed(processed, out_dir)
    print(f"[✅] Processed {len(processed)} tickets → {out_dir}")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python ingest.py <raw_dir> <out_dir>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
