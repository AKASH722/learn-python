import socket

host = socket.gethostname()
port = 8000
ADDR = host, port
server = socket.socket(type=socket.SOCK_DGRAM)
server.bind(ADDR)
while True:
    rep, addr = server.recvfrom(1024)
    if not rep: break
    print(f'client({addr}) --> {rep.decode()}')
    msg = input('server --> ')
    server.sendto(msg.encode(), addr)
    if not msg: break
server.close()
