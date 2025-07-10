#!/usr/bin/env python3
"""
extract_iban.py
---------------
Professional tool to extract unique IBANs from financial transaction files (e.g. .fin, .txt, .csv).
Fully documented for security audits and operational traceability.

Usage:
    python extract_iban.py --input yourfile.fin --output ibans.txt

Requirements:
    - Python 3.7+
    - No external dependencies (uses only Python Standard Library)

Author: OCOS Security Team
Date: 2025-07-10
"""

import argparse
import re
import logging
import sys
from typing import Set

# Configure logging for audit trail
logging.basicConfig(
    filename='extract_iban.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Regular expression for IBAN (generic, all countries)
IBAN_REGEX = r'\b[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}\b'


def extract_ibans_from_file(input_file: str) -> Set[str]:
    """
    Extract all unique IBANs from the given file.

    Args:
        input_file (str): Path to the input file.

    Returns:
        Set[str]: Set of unique IBANs found in the file.
    """
    ibans = set()
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line_number, line in enumerate(f, start=1):
                matches = re.findall(IBAN_REGEX, line)
                if matches:
                    ibans.update(matches)
    except Exception as e:
        logging.error(f"Failed to extract IBANs from {input_file}: {e}")
        raise
    logging.info(f"Extracted {len(ibans)} unique IBAN(s) from {input_file}")
    return ibans


def write_ibans_to_file(ibans: Set[str], output_file: str) -> None:
    """
    Write IBANs to output file, one per line.

    Args:
        ibans (Set[str]): Set of IBANs to write.
        output_file (str): Output file path.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for iban in sorted(ibans):
                f.write(f"{iban}\n")
    except Exception as e:
        logging.error(f"Failed to write IBANs to {output_file}: {e}")
        raise
    logging.info(f"Wrote {len(ibans)} IBAN(s) to {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Extract unique IBANs from a financial transaction file."
    )
    parser.add_argument('--input', '-i', required=True, help="Input file (e.g. .fin, .txt, .csv)")
    parser.add_argument('--output', '-o', required=True, help="Output file for extracted IBANs")

    args = parser.parse_args()

    logging.info(f"Started IBAN extraction: input={args.input}, output={args.output}")
    try:
        ibans = extract_ibans_from_file(args.input)
        if not ibans:
            print("No IBANs found in the input file.")
            logging.warning("No IBANs found.")
        else:
            write_ibans_to_file(ibans, args.output)
            print(f"Extraction complete: {len(ibans)} IBAN(s) written to {args.output}")
    except Exception as err:
        print(f"Error: {err}")
        sys.exit(1)
    logging.info("IBAN extraction script completed successfully.")


if __name__ == '__main__':
    main()
