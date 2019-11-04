import socket
def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'I LOVE JINGJING'
    data = text.encode()
    addr=('127.0.0.1', 3307)
    sock.sendto(data, addr)

    data, addr = sock.recvfrom(200)
    textrecv= data.decode()
    print(textrecv)


if __name__ == '__main__':
    print('START...')
    client()
    print('END...')