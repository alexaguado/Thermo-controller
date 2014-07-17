import socket, threading
from clienttelnet import chatServer
from XMLReader import XMLReader
import sys

config = XMLReader('../config/config.xml')

HOST = config.getTelnetIP()
PORT = int(config.getTelnetPort()) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)

class mainServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    	print "Starting Telnet"
    	sys.stdout.flush()

    def run(self):
		while True: 
			chatServer(s.accept()).start()
