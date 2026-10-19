import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 5001))
with open("data.txt", "rb") as f:
        data = f.read()



client_socket.sendall(data)

client_socket.close()

print("File sent successfully!")