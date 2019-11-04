import socket

def serverFunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    addr = ("127.0.0.1", 7852)
    sock.bind(addr)
    #接受到的数据和对方的地址
    data, addr = sock.recvfrom(500)
    text = data.decode()
    print(text)
    rsp = "Ich hab keine Hunge"
    data = rsp.encode()
    sock.sendto(data, addr)

if __name__ == '__main__':
    print('Starting.......')
    serverFunc()
    print('Ending.......')
