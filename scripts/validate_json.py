#!/usr/bin/env python3
"""
validate_json.py

Professional JSON structure and schema validation script.
- Validates any JSON file against a given schema.
- Supports audit, compliance, and data integrity in blockchain workflows.

Author: OCOS Team | 2025

Usage:
    python validate_json.py <json_file> <schema_file>
"""

import sys
import json
from jsonschema import validate, ValidationError

def load_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error loading {filename}: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    json_file, schema_file = sys.argv[1], sys.argv[2]
    data = load_json(json_file)
    schema = load_json(schema_file)

    try:
        validate(instance=data, schema=schema)
        print(f"✅ {json_file} is valid according to {schema_file}")
        sys.exit(0)
    except ValidationError as ve:
        print(f"❌ {json_file} is INVALID:\n{ve.message}")
        sys.exit(2)
    except Exception as e:
        print(f"❌ Validation error: {e}")
        sys.exit(3)

if __name__ == "__main__":
    main()
