import  socket

def clientFunc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'I love jingjing'
    data = text.encode()

    #send
    sock.sendto(data, ('127.0.0.1', 7852))
    data, addr = sock.recvfrom(200)
    data = data.decode()
    print(data)
if __name__ == '__main__':
    clientFunc()
