#!/usr/bin/env python3
"""
Decryption Module.

This module provides functions for encrypting data using the cryptography library.
"""
from cryptography.fernet import Fernet

def encrypt(data):
    """
    Encrypts the given data.

    Args:
        data (str): The plain text data to encrypt.

    Returns:
        bytes: The encrypted data.
    """
    if isinstance(data, str):
        data = data.encode()
    key = load_key('./client_app/key/encryption_key.key')
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)
    return encrypted_data

def load_key(file_path):
    """
    Loads the encryption key from a file.

    Args:
        file_path (str): Path to the file containing the encryption key.

    Returns:
        bytes: The encryption key.
    """
    with open(file_path, 'rb') as key_file:
        key = key_file.read()
    return key
