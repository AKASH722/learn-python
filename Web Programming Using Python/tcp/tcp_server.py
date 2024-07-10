import socket
host = socket.gethostname() #as both run on same computer
port = 5000
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen()
conn, address = server_socket.accept()
print("Connection from", str(address))
while True: 
    data = conn.recv(1024).decode()
    if not data: break
    print("client:", data)
    msg = input("server: ")
    conn.send(msg.encode())
conn.close()