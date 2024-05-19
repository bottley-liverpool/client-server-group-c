# Project Specifications: Client/Server Network System

## 1. Project Overview

This project involves developing a simple client/server network system with functionalities for sending serialised data and encrypted text files. The client should be able to serialise data into multiple formats and encrypt text files. At the same time, the server should be able to deserialise and decrypt the received data and display or store it accordingly.

### Objectives
- Develop a client application to serialise a dictionary and send text files.
- Develop a server application to receive serialised data, decrypt data, and manage outputs.
- Implement user options for different serialisation formats and encryption of text files.
- Ensure the system is robust and has proper error handling and unit testing.

## 2. System Architecture

### Client Components
- **Serialization Module**: Handles the serialisation of dictionary data into binary, JSON, or XML format.
- **Encryption Module**: Responsible for encrypting text files before sending them to the server.
- **Networking Module**: Manages sending serialised data and encrypted files to the server.

### Server Components
- **Networking Module**: Receives data from the client.
- **Decryption Module**: Decrypts the received encrypted files.
- **Deserialization Module**: Converts serialised data back into usable formats.
- **Data Handler**: Optionally displays data on the screen or writes it to a file, configurable by the server settings.

### Data Flow
- Data is serialised and optionally encrypted on the client side before transmission.
- The server receives, decrypts, and deserialises the data, then processes it according to configuration.

## 3. Technologies Used
- **Programming Language**: Python 3.8+
- **Libraries**: 
  - `socket` for networking
  - `pickle`, `JSON`, for serialisation
  - `xml.etree.ElementTree` for XML handling
  - `cryptography` for encryption
- **Tools**:
  - Git for version control
  - draw.io for architecture diagrams
  - Streamlit for interactive UI components

## 4. Functional Requirements

### Client
The user should be able to input a dictionary and select a serialisation format.
- User should be able to input text, opt for encryption, and send it to the server.
- Handle errors related to network issues or serialisation.

### Server
- Capable of running continuously and handling multiple client connections.
- Decrypt and deserialise received data.
- Configurable to display data or save it to a file.

## 5. Security Requirements
- Implement standard encryption for all transmitted files.
- Ensure secure transmission channels are used (e.g., using SSL/TLS for added security).

## 6. Testing
- Unit tests for each module (serialisation, encryption, networking, deserialisation, decryption).
- Integration tests verify that the whole system works as expected.

## 7. Project Management
- **Timeline**: 2 weeks from initiation to deployment.
- **Roles**:
  - Project Manager
  - Developers
  - QA - Testers
- **Meetings**: 3 team meetings to plan and discuss progress and any issues.

## 8. Documentation
- Complete documentation for each component's functionality and interactions.
- User manual on how to set up and use the system.

## 9. Version Control
- Regular commits to the Git repository with meaningful commit messages describing changes and updates.
- Feature branching strategy to manage developments.

## 10. Deployment
- Final testing and deployment on a test server before production deployment.
