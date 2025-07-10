#!/usr/bin/env python3
"""
validate_iban.py

Professional IBAN validator using Modulo 97 algorithm.
Audit-ready, supports batch and single IBAN validation.
Author: OCOS Team | 2025
"""

import re
import sys

IBAN_REGEX = re.compile(r'^[A-Z]{2}\d{2}[A-Z0-9]{11,30}$')

def iban_to_numeric(iban):
    """Convert IBAN to numeric representation for modulo calculation."""
    rearranged = iban[4:] + iban[:4]
    converted = ''
    for char in rearranged:
        if char.isdigit():
            converted += char
        else:
            converted += str(ord(char.upper()) - 55)  # A=10, B=11, ..., Z=35
    return converted

def validate_iban(iban):
    """Validate an IBAN using regex and Modulo 97 check."""
    iban = iban.replace(' ', '').upper()
    if not IBAN_REGEX.match(iban):
        return False, "IBAN format is invalid"
    numeric_iban = iban_to_numeric(iban)
    if int(numeric_iban) % 97 != 1:
        return False, "Modulo 97 check failed"
    return True, "Valid IBAN"

def batch_validate_ibans(file_path):
    """Validate a list of IBANs from a file."""
    with open(file_path, 'r') as f:
        ibans = [line.strip() for line in f if line.strip()]
    results = []
    for iban in ibans:
        valid, msg = validate_iban(iban)
        results.append((iban, valid, msg))
    return results

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].endswith('.txt'):
        # Batch mode: validate IBANs from file
        file_path = sys.argv[1]
        results = batch_validate_ibans(file_path)
        for iban, valid, msg in results:
            print(f"{iban}: {'OK' if valid else 'INVALID'} - {msg}")
    elif len(sys.argv) == 2:
        # Single IBAN validation
        iban = sys.argv[1]
        valid, msg = validate_iban(iban)
        print(f"{iban}: {'OK' if valid else 'INVALID'} - {msg}")
    else:
        print("Usage:")
        print("  python validate_iban.py AZ21NABZ00000000137010001944")
        print("  python validate_iban.py ibans.txt")
