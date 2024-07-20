import socket

host = socket.gethostname()
port = 8000
ADDR = host, port
client = socket.socket(type=socket.SOCK_DGRAM)
while True:
    msg = input('client --> ')
    client.sendto(msg.encode(), ADDR)
    if not msg: break
    rep, ADDR = client.recvfrom(1024)
    rep = rep.decode()
    if not rep: break
    print(f'server({ADDR}) --> {rep}')
client.close()
