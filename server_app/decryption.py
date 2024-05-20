#!/usr/bin/env python3
"""
Decryption Module.

This module provides functions for decrypting data using the cryptography library.
"""

from cryptography.fernet import Fernet

def decrypt(data):
    """
    Decrypts the given data.

    Args:
        data (bytes): The encrypted data to decrypt.

    Returns:
        str: The decrypted plaintext data.
    """
    key = load_key('./key/encryption_key.key')
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(data)
    return decrypted_data.decode()  # Convert bytes back to string

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
