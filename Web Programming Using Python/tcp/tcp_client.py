import socket

# host = socket.gethostname() #as both run on same computer
host = '192.168.93.138'
port = 5000
client_socket = socket.socket()
client_socket.connect((host, port))
msg = input("client: ")
while msg.lower().strip() != "bye":
    client_socket.send(msg.encode())
    print("server:", client_socket.recv(1024).decode())
    msg = input("client: ")
client_socket.close()
