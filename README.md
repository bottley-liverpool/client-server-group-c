
# Client-Server Group Project

## Project Overview

This project demonstrates a simple client-server network built with Python. The client can send dictionaries and text files to the server, with options for serialization and encryption. The server receives the data, processes it, and logs the results. The client interface is built using Streamlit.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Testing](#testing)
- [License](#license)

## Features

- **Dictionary Handling**: Send serialized dictionaries in binary, JSON, or XML formats.
- **Text File Handling**: Send text files with optional encryption.
- **Encryption**: Use Fernet encryption for secure text file transmission.
- **Logging**: Configurable server logging to screen and/or file.
- **Client Interface**: Streamlit-based user interface for client operations.
- **Server**: Handles incoming data and processes it accordingly.

## Project Structure

```
client-server-group-c/
├── client_app/
│   ├── __init__.py
│   ├── app.py
│   ├── encryption.py
│   ├── networking.py
│   ├── serialization.py
│   ├── key/ (contains encryption_key.key)
│   ├── tests/ 
│       ├── test_app.py
│       ├── test_encryption.py
│       ├── test_networking.py
│       ├── test_serialization.py
├── server_app/
│   ├── __init__.py
│   ├── server.py
│   ├── decryption.py
│   ├── deserialization.py
│   ├── config.json
│   ├── key/ (contains encryption_key.key)
│   ├── tests/ 
│       ├── test_decryption.py
│       ├── test_deserialization.py
│       ├── test_server.py
├── docs/
│   ├── CSCK541_GroupC_SysArch.drawio
│   ├── directory_tree.txt
│   ├── LICENSE.txt
│   ├── SPECIFICATIONS.md
│   ├── tech_stack.md
├── main.py
├── README.md
├── requirements.txt
```

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/bottley-liverpool/client-server-group-c.git
    cd client-server-group-c
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Server Logging**:
    Edit `server_app/config.json` to configure logging:
    ```json
    {
        "log_to_screen": true,
        "log_to_file": true,
        "log_file_path": "server_log.txt"
    }
    ```

## Usage

1. **Run the Server and Client**:
    Start the server and client using the `main.py` script:
    ```bash
    python3 main.py
    ```

2. **Use the Client Interface**:
    Open the Streamlit interface in your web browser (usually at `http://localhost:8501`) and perform actions like sending dictionaries and text files.

## Testing

1. **Run Unit Tests**:
    Use `unittest` to run the tests for both client and server modules:
    ```bash
    python3 -m unittest discover -s tests
    ```
2. **Run Coverage Report**:
    ```bash
    coverage report -m
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](docs/LICENSE.md) file for details.