import socket

def server():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    addr = ('127.0.0.1', 3307)
    sock.bind(addr)

    data,addr = sock.recvfrom(500)

    text = data.decode()
    print(text)
    rsp = 'hahahahaaha'

    data = rsp.encode()

    sock.sendto(data,addr)


if __name__ == '__main__':
    import  time
    while True:
        try:
            print('Starting...')
            server()
            print('Ending...')
        except Exception as e:
            print(e)
        time.sleep(1)
