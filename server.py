
import socket


def start_server(
    host="0.0.0.0",
    port=5001,
    filename="data.txt",
    buffer_size=4096
):
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server started on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    with open(filename, "wb") as f:
        while True:
            bytes_read = conn.recv(buffer_size)

            if not bytes_read:
                break

            f.write(bytes_read)

    conn.close()
    server_socket.close()

    print(f"File saved as {filename}")


start_server()

