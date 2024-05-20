"""
Networking unit tests module
"""
import unittest
import socket
from unittest.mock import patch, mock_open, MagicMock
from client_app.networking import connect_server, send_command, send_dictionary, send_text_file

class TestNetworking(unittest.TestCase):
    """
    Test the networking functions
    """
    @patch('client_app.networking.socket.socket')
    def test_connect_server(self, mock_socket):
        """
        Test connecting to the server
        """
        mock_socket_instance = MagicMock()
        mock_socket.return_value = mock_socket_instance

        client_socket = connect_server()

        mock_socket.assert_called_with(socket.AF_INET, socket.SOCK_STREAM)
        mock_socket_instance.connect.assert_called_with(('127.0.0.1', 5005))
        self.assertEqual(client_socket, mock_socket_instance)

    @patch('client_app.networking.connect_server')
    def test_send_command(self, mock_connect_server):
        """
        Test sending a command to the server
        """
        mock_client_socket = MagicMock()
        mock_connect_server.return_value = mock_client_socket

        send_command(mock_client_socket, 'test_command')

        mock_client_socket.sendall.assert_called_with(b'test_command\n')

    @patch('client_app.networking.connect_server')
    @patch('client_app.networking.serialize')
    def test_send_dictionary(self, mock_serialize, mock_connect_server):
        """
        Test serializing and sending a dictionary to the server
        """
        mock_client_socket = MagicMock()
        mock_connect_server.return_value = mock_client_socket
        mock_serialize.return_value = b'serialized_data'

        data = {'key': 'value'}
        serialization_format = 'json'
        send_dictionary(data, serialization_format)

        mock_connect_server.assert_called_once()
        mock_serialize.assert_called_once_with(data, serialization_format)
        mock_client_socket.sendall.assert_any_call(b'dictionary\n')
        mock_client_socket.sendall.assert_any_call(b'json\n')
        mock_client_socket.sendall.assert_any_call(b'serialized_data')
        mock_client_socket.close.assert_called_once()

    @patch('client_app.networking.connect_server')
    @patch('client_app.networking.encrypt')
    @patch('builtins.open', new_callable=mock_open, read_data=b'test file data')
    def test_send_text_file_encrypted(self, mock_file, mock_encrypt, mock_connect_server):
        """
        Test reading, encrypting, and sending a text file to the server
        """
        mock_client_socket = MagicMock()
        mock_connect_server.return_value = mock_client_socket
        mock_encrypt.return_value = b'encrypted_data'

        file_path = 'test.txt'
        encrypt_data = True
        send_text_file(file_path, encrypt_data)

        mock_connect_server.assert_called_once()
        mock_file.assert_called_once_with(file_path, 'rb')
        mock_encrypt.assert_called_once_with(b'test file data')
        mock_client_socket.sendall.assert_any_call(b'text_file\n')
        mock_client_socket.sendall.assert_any_call(b'True\n')
        mock_client_socket.sendall.assert_any_call(b'encrypted_data')
        mock_client_socket.close.assert_called_once()

    @patch('client_app.networking.connect_server')
    @patch('builtins.open', new_callable=mock_open, read_data=b'test file data')
    def test_send_text_file_plain_text(self, mock_file, mock_connect_server):
        """
        Test reading and sending a plain text file to the server
        """
        mock_client_socket = MagicMock()
        mock_connect_server.return_value = mock_client_socket

        file_path = 'test.txt'
        encrypt_data = False
        send_text_file(file_path, encrypt_data)

        mock_connect_server.assert_called_once()
        mock_file.assert_called_once_with(file_path, 'rb')
        mock_client_socket.sendall.assert_any_call(b'text_file\n')
        mock_client_socket.sendall.assert_any_call(b'False\n')
        mock_client_socket.sendall.assert_any_call(b'test file data')
        mock_client_socket.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()
