"""
Networking module to send commands, dictionaries & text files
"""
import socket
from client_app.serialization import serialize
from client_app.encryption import encrypt

# Server host & port number
HOST = '127.0.0.1'
PORT = 5005

def connect_server():
    """
    Connects to the server

    Returns:
        client_socket (socket.socket): The socket connected to the server.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    return client_socket

def send_command(client_socket, command):
    """
    Sends a command to the server.
    
    Args:
        command (str): The command to send.
    """
    client_socket.sendall((command + '\n').encode())

def send_dictionary(data, serialization_format):
    """
    Serializes and sends a dictionary to the server.
    
    Args:
        data (dict): The dictionary to send.
        serialization_format (str): The format to serialize the data into ('binary', 'json', 'xml').
    """
    client_socket = connect_server()
    send_command(client_socket, "dictionary")
    serialized_data = serialize(data, serialization_format)
    client_socket.sendall((serialization_format + '\n').encode())
    client_socket.sendall(serialized_data)
    client_socket.close()

def send_text_file(file_path, encrypt_data):
    """
    Reads, encrypts (if needed), and sends a text file to the server.
    
    Args:
        client_socket (socket.socket): The socket connected to the server.
        file_path (str): Path to the text file to send.
        encrypt_data (bool): Whether to encrypt the file data before sending.
    """
    client_socket = connect_server()
    send_command(client_socket, "text_file")

    with open(file_path, 'rb') as file:
        data = file.read()

    if encrypt_data:
        data = encrypt(data)
        client_socket.sendall(b'True\n')
    else:
        client_socket.sendall(b'False\n')

    client_socket.sendall(data)
    client_socket.close()
