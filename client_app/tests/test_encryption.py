"""
Encryption unit tests module
"""
import unittest
from unittest.mock import patch, mock_open
from cryptography.fernet import Fernet
from client_app.encryption import encrypt, load_key

class TestEncryption(unittest.TestCase):
    """
    Test the encryption functions
    """
    def setUp(self):
        """
        Set up test data for encryption
        """
        self.test_data = "This is a test."
        self.encrypted_data = b"encrypted_data"
        self.key = Fernet.generate_key()

    @patch("builtins.open", new_callable=mock_open, read_data=b"test_key")
    def test_load_key(self, mock_file):
        """
        Test loading the key from a file
        """
        key = load_key('./client_app/key/encryption_key.key')
        mock_file.assert_called_with('./client_app/key/encryption_key.key', 'rb')
        self.assertEqual(key, b"test_key")

    @patch("builtins.open", new_callable=mock_open, read_data=b"test_key")
    @patch("cryptography.fernet.Fernet.encrypt")
    @patch("client_app.encryption.load_key")
    def test_encrypt(self, mock_load_key, mock_encrypt, mock_file):
        """
        Test encrypting data
        """
        mock_load_key.return_value = self.key
        mock_encrypt.return_value = self.encrypted_data
        
        result = encrypt(self.test_data)
        mock_load_key.assert_called_once_with('./client_app/key/encryption_key.key')
        mock_encrypt.assert_called_once()
        self.assertEqual(result, self.encrypted_data)

if __name__ == "__main__":
    unittest.main()
