import socket
import hashlib
import sys


PORT = 7039

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', PORT))



def listen():
	while True:
		message, cadrs = server.recvfrom(65507)
		dmes = message.decode()
		print(dmes)
		print(type(dmes))


listen()


