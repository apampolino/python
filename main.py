from threading import Thread
import sys
import os
import socket


def handle_recv(conn, addr):
    print('Started Thread on host %s port %i' % addr)
    with conn:
        while True:
            buf = conn.recv(1024)
            print(buf)
            if not buf:
                break
            conn.sendall(b'Thank you')
    print('Exiting Thread on host %s port %i' % addr)


if __name__ == '__main__':
    threads = []
    connections = []

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 7999))
    print('Server started on %s on port %i' % ('127.0.0.1', 7999))
    while True:
        s.listen(10)
        conn, addr = s.accept()
        if conn:
            print('Connection accepted on host %s port %i' % addr)
            t = Thread(target=handle_recv(conn, addr))
            t.start()
            threads.append(t)

    for t in threads:
        t.join()

    s.close()
    print('Exiting MainThread')
    exit(0)
