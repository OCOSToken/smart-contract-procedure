#!/usr/bin/env python3
"""
convert_fiat.py

Description:
    Parses a SWIFT FIN (MT) file and extracts transaction details, converting them
    into a standardized fiat transaction format (CSV or JSON). Output includes
    IBAN, amount, currency, transaction reference, date, and sender/receiver.

Usage:
    python convert_fiat.py <input_fin_file> <output_file.csv>

Author: OCOS Team
License: Apache 2

Example:
    python convert_fiat.py sample.fin output.csv

Dependencies:
    - Python 3.x

Security Notice:
    Do not include or expose any sensitive private keys or credentials in logs or outputs.
"""

import re
import sys
import csv

def parse_fin(file_path):
    # Example: simple parser for MT103 fields (customize for your SWIFT FIN format)
    with open(file_path, 'r') as f:
        data = f.read()

    # Extract example fields
    transactions = []
    pattern = re.compile(
        r":20:(?P<reference>[^\n]+).*?:32A:(?P<date>\d{6})(?P<currency>[A-Z]{3})(?P<amount>[\d,]+).*?:50[AK]?:([^\n]+).*?:59:([^\n]+).*?",
        re.DOTALL
    )

    for match in pattern.finditer(data):
        transactions.append({
            'Reference': match.group('reference').strip(),
            'Date': match.group('date').strip(),
            'Currency': match.group('currency').strip(),
            'Amount': match.group('amount').replace(',', '.').strip(),
            'Sender': match.group(6).strip() if match.group(6) else "",
            'Receiver': match.group(7).strip() if match.group(7) else "",
        })
    return transactions

def save_as_csv(transactions, output_file):
    if not transactions:
        print("No transactions found.")
        return

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = transactions[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for tx in transactions:
            writer.writerow(tx)
    print(f"Saved {len(transactions)} transactions to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_fiat.py <input_fin_file> <output_file.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    transactions = parse_fin(input_file)
    save_as_csv(transactions, output_file)
