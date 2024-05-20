#!/usr/bin/env python3
"""
Local Server Module
"""
import socket
import json
from server_app.decryption import decrypt
from server_app.deserialization import deserialize

HOST = '127.0.0.1' # Server Host
PORT = 5005 # Server Port

# Config file for server logging
CONFIG_PATH = './server_app/config.json'
with open(CONFIG_PATH, 'r', encoding="utf-8") as config_file:
    config = json.load(config_file)

LOG_TO_SCREEN = config.get('log_to_screen', True)
LOG_TO_FILE = config.get('log_to_file', True)
LOG_FILE_PATH = config.get('log_file_path', 'server_log.txt')

def log_message(message):
    """
    Logs the given message based on the configuration settings.

    Args:
        message (str): The message to log.
    """
    if LOG_TO_SCREEN:
        print(message)
    if LOG_TO_FILE:
        with open(LOG_FILE_PATH, 'a', encoding="utf-8") as log_file:
            log_file.write(message + '\n')

def handle_dictionary(data, serialization_format):
    """
    Handle received dictionary based on serialization format.

    Args:
        data (bytes): Serialized dictionary data.
        serialization_format (str): Format of the serialized data ('binary', 'json', 'xml').

    Returns:
        dict: Deserialized dictionary.
    """
    return deserialize(data, serialization_format)

def handle_text_file(data, is_encrypted):
    """
    Handle received text file.

    Args:
        data (bytes): Text file data.
        is_encrypted (bool): Flag indicating if the data is encrypted.

    Returns:
        str: Decrypted or plain text.
    """
    if is_encrypted:
        try:
            text = decrypt(data)
            log_message(f"Decrypted text: {text}")
        except Exception as e:
            log_message(f"Decryption failed: {e}")
            text = "Decryption failed"
    else:
        text = data.decode()
    return text

def handle_client(client_socket):
    """
    Handle client requests.

    Args:
        client_socket (socket.socket): The socket connected to the client.
    """
    try:
        command = client_socket.recv(1024).strip().decode()
        log_message(f"Received command: {command}")

        if command == "dictionary":
            serialization_format = client_socket.recv(1024).strip().decode()
            log_message(f"Serialization format: {serialization_format}")

            data = b''
            while True:
                packet = client_socket.recv(4096)
                if not packet:
                    break
                data += packet
                log_message(f"Received packet: {packet}")

            dictionary = handle_dictionary(data, serialization_format)
            log_message(f"Received dictionary: {dictionary}")
        elif command == "text_file":
            is_encrypted_str = client_socket.recv(1024).strip().decode()
            is_encrypted = is_encrypted_str == "True"
            log_message(f"Is encrypted: {is_encrypted}")

            data = b''
            while True:
                packet = client_socket.recv(4096)
                if not packet:
                    break
                data += packet
                log_message(f"Received packet: {packet}")

            text = handle_text_file(data, is_encrypted)
            log_message(f"Received text file: {text}")
        else:
            log_message("Invalid command")
    except Exception as e:
        log_message(f"Error handling client: {e}")
    finally:
        client_socket.close()

def main():
    """
    Main function to start the server.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    log_message(f"Server is listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        log_message(f"Connected to {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
