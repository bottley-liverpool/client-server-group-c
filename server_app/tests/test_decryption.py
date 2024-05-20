"""
Decryption unit tests module
"""
import unittest
from unittest.mock import patch, mock_open
from cryptography.fernet import Fernet
from server_app.decryption import decrypt, load_key

class TestDecryption(unittest.TestCase):
    """
    Test the load_key & decrypt functions
    """
    def setUp(self):
        """
        Generate a key and encrypt some data for testing
        """
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
        self.test_data = b"This is a test."
        self.encrypted_data = self.cipher_suite.encrypt(self.test_data)
        self.key_path = './key/encryption_key.key'
        self.mock_key = Fernet.generate_key()

    @patch("builtins.open", new_callable=mock_open)
    def test_load_key(self, mock_file):
        """
        Test loading the key from a file
        """
        mock_file.return_value.read.return_value = self.mock_key
        key = load_key(self.key_path)
        mock_file.assert_called_with(self.key_path, 'rb')
        self.assertEqual(key, self.mock_key)

    @patch("builtins.open", new_callable=mock_open)
    @patch("cryptography.fernet.Fernet.decrypt")
    def test_decrypt(self, mock_decrypt, mock_file):
        """
        Test decrypting data
        """
        mock_file.return_value.read.return_value = self.mock_key
        mock_decrypt.return_value = self.test_data
        decrypted_data = decrypt(self.encrypted_data)
        self.assertEqual(decrypted_data, self.test_data.decode())
        mock_file.assert_called_with('./key/encryption_key.key', 'rb')
        mock_decrypt.assert_called_once_with(self.encrypted_data)

if __name__ == "__main__":
    unittest.main()
