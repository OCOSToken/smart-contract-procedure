#!/usr/bin/env python3
"""
encrypt_aes.py

AES-256-CBC file encryption and decryption utility.
Professional security script for audit-ready workflows.
Author: OCOS Team | 2025

Requirements:
    pip install pycryptodome

Usage:
    Encrypt: python encrypt_aes.py encrypt <input_file> <output_file> <password>
    Decrypt: python encrypt_aes.py decrypt <input_file> <output_file> <password>
"""

import sys
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK_SIZE = 16

def pad(data):
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    pad_len = data[-1]
    if pad_len < 1 or pad_len > BLOCK_SIZE:
        raise ValueError("Invalid padding.")
    return data[:-pad_len]

def derive_key_iv(password):
    key = hashlib.sha256(password.encode()).digest()  # 32 bytes for AES-256
    iv = hashlib.md5(password.encode()).digest()       # 16 bytes for IV
    return key, iv

def encrypt_file(input_path, output_path, password):
    key, iv = derive_key_iv(password)
    with open(input_path, 'rb') as f:
        plaintext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext))
    with open(output_path, 'wb') as f:
        f.write(ciphertext)
    print(f"Encrypted: {input_path} → {output_path}")

def decrypt_file(input_path, output_path, password):
    key, iv = derive_key_iv(password)
    with open(input_path, 'rb') as f:
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext))
    with open(output_path, 'wb') as f:
        f.write(plaintext)
    print(f"Decrypted: {input_path} → {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 5 or sys.argv[1] not in ["encrypt", "decrypt"]:
        print(__doc__)
        sys.exit(1)

    mode, input_file, output_file, password = sys.argv[1:5]
    if len(password) < 12:
        print("⚠️  Password should be at least 12 characters for security.")
        sys.exit(2)

    if mode == "encrypt":
        encrypt_file(input_file, output_file, password)
    elif mode == "decrypt":
        decrypt_file(input_file, output_file, password)
