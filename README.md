# Python TCP File Transfer

A simple client-server file transfer application built using Python's built-in `socket` module. It uses TCP (Transmission Control Protocol) to transfer a file from a client to a server over a network.

## Features

- Transfer files using TCP sockets.
- Send binary files using `rb` mode.
- Receive files in chunks to avoid loading the entire file into server memory.
- Save received data to a file on the server.
- Uses Python's standard library; no external dependencies required.

## Project Structure

```text
python-tcp-file-transfer/
├── client.py
├── server.py
├── data.txt
└── README.md
```

## Requirements

- Python 3.8 or later
- Two terminal windows
- Client and server running on the same computer or network

## How It Works

1. The server creates a TCP socket and listens on port `5001`.
2. The client connects to the server.
3. The client reads `data.txt` in binary mode.
4. The client sends the file contents through the TCP connection.
5. The server receives the data in chunks of up to 4096 bytes.
6. The server writes the received bytes to a file.

## Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/KrishnansuMohapatra/Networking-Projects/tree/main/File%20transfer

```


### 2. Prepare the File

Place the file you want to transfer in the same directory as `client.py`. By default, the client sends `data.txt`.

### 3. Start the Server

Open a terminal and run:

```bash
python server.py
```

Expected output:

```text
Server started on 0.0.0.0:5001
```

### 4. Run the Client

Open another terminal in the project directory and run:

```bash
python client.py
```

Expected client output:

```text
File sent successfully!
```

The server displays the client's connection information and saves the received file as `data.txt`.

## Configuration

The server function supports these parameters:

| Parameter | Default | Description |
|---|---|---|
| `host` | `0.0.0.0` | Listens on all available IPv4 interfaces |
| `port` | `5001` | TCP port |
| `filename` | `data.txt` | Destination filename |
| `buffer_size` | `4096` | Maximum bytes received per `recv()` call |

The client connects to `127.0.0.1:5001`, which refers to the local computer. For transfers between different computers, replace `127.0.0.1` with the server's reachable IP address and configure the network firewall appropriately.

## Technologies Used

- **Python** — programming language
- **Socket Programming** — network communication
- **TCP/IP** — reliable, ordered byte-stream transport
- **File Handling** — reading and writing binary data

## Learning Objectives

This project demonstrates:

- Client-server architecture
- TCP socket creation and connection
- Binding and listening on a port
- Sending and receiving bytes
- Binary file handling
- Buffer-based data processing
- Basic network programming in Python

## Limitations

- The current server handles one client connection per execution.
- The client reads the entire file into memory.
- The destination file may be overwritten if it already exists.
- There is no application-level acknowledgment to verify that the complete file was saved.
- The connection does not provide encryption or authentication.

**Security note:** Use this implementation only in a trusted environment. Do not expose it directly to untrusted networks without adding authentication, encryption, file-size limits, and appropriate validation.

## Future Improvements

- Add chunk-based file reading on the client.
- Support multiple client connections.
- Add transfer progress and file-size reporting.
- Implement error handling and application-level acknowledgments.
- Add file integrity verification using SHA-256.
- Support secure transfers using TLS.

## License

This project is available for educational and personal learning purposes. Add a license file if you intend to distribute it under specific reuse terms.
