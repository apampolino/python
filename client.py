import socket
import time
from threading import Thread


def send(s, message=None):
    while True:
        s.sendall(b'Hello, world')
        time.sleep(1)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 7999))
    t = Thread(target=send(s))
    t.start()

    while True:
        data = s.recv(1024)
        print(data)
        if data:
            print(data)

    t.join()
    s.close()
