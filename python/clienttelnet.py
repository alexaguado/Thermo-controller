import socket, threading
from getRedis import GetRedis
import sys

clients = [] #list of clients connected
lock = threading.Lock()


class chatServer(threading.Thread):
    def __init__(self, (socket,address)):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address= address

    def run(self):
        lock.acquire()
        clients.append(self)
        lock.release()
        print '%s:%s connected.' % self.address
        sys.stdout.flush()
        for c in clients:
            c.socket.send('\n\n\nWELCOME TO THE THERMO CONTROLLER:\n')
        while True:
            for c in clients:
                c.socket.send('\n\n\n\nOPTIONS:\n')
                c.socket.send('1. See the last commit\n')
                c.socket.send('2. See current temperature\n')
                c.socket.send('quit\n')
            data = self.socket.recv(1024)
            if not data:
                break
            if "quit" in data:
                break
            if "1" in data:
                for c in clients:
                    rediscli = GetRedis()
                    commit = rediscli.get(1)
                    c.socket.send("\nResult::: "+commit+"\n")
            if "2" in data:
                for c in clients:
                    rediscli = GetRedis()
                    commit = rediscli.get(2)
                    c.socket.send("\nResult::: "+commit+"\n")
        self.socket.close()
        print '%s:%s disconnected.' % self.address
        sys.stdout.flush()
        lock.acquire()
        clients.remove(self)
        lock.release()