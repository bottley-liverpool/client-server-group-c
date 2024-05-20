"""
Server unit tests module
"""
import unittest
from unittest.mock import patch, MagicMock, mock_open
from server_app.local_server import handle_client, handle_dictionary, handle_text_file, log_message

class TestServer(unittest.TestCase):
    """
    Test the server functions
    """
    @patch('server_app.local_server.deserialize')
    def test_handle_dictionary(self, mock_deserialize):
        """
        Test the handle_dictionary function
        """
        mock_deserialize.return_value = {'key': 'test', 'value': 30}
        data = b'test_data'
        serialization_format = 'json'
        result = handle_dictionary(data, serialization_format)
        mock_deserialize.assert_called_once_with(data, serialization_format)
        self.assertEqual(result, {'key': 'test', 'value': 30})

    @patch('server_app.local_server.decrypt')
    def test_handle_text_file_encrypted(self, mock_decrypt):
        """
        Test the handle_text_file function with encrypted data
        """
        mock_decrypt.return_value = 'Decrypted text'
        data = b'encrypted_data'
        is_encrypted = True
        result = handle_text_file(data, is_encrypted)
        mock_decrypt.assert_called_once_with(data)
        self.assertEqual(result, 'Decrypted text')

    def test_handle_text_file_not_encrypted(self):
        """
        Test the handle_text_file function with plain text data
        """
        data = b'plain_text_data'
        is_encrypted = False
        result = handle_text_file(data, is_encrypted)
        self.assertEqual(result, 'plain_text_data')

    @patch('server_app.local_server.log_message')
    @patch('socket.socket')
    def test_handle_client(self, mock_socket, mock_log_message):
        """
        Test the handle_client function
        """
        mock_client_socket = MagicMock()
        mock_client_socket.recv.side_effect = [
            b'dictionary\n',
            b'json\n',
            b'{"key": "test", "value": 30}',
            b''
        ]

        handle_client(mock_client_socket)

        mock_log_message.assert_any_call('Received command: dictionary')
        mock_log_message.assert_any_call('Serialization format: json')
        mock_log_message.assert_any_call('Received packet: b\'{"key": "test", "value": 30}\'')

    @patch('server_app.local_server.log_message')
    @patch('builtins.open', new_callable=mock_open, read_data='{"log_to_screen": true, "log_to_file": true, "log_file_path": "server_log.txt"}')
    def test_log_message(self, mock_file, mock_log_message):
        """
        Test the log_message function
        """
        message = 'Test log message'
        log_message(message)

        if mock_log_message.called:
            mock_log_message.assert_called_with(message)
        
        mock_file().write.assert_called_with(message + '\n')

if __name__ == "__main__":
    unittest.main()
