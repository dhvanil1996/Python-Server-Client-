import sys
import socket
import hashlib
		
 
buffersize = 32768
PORT = 7044
MAX_UDP_PAYLOAD = 65507
 

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', PORT))

def md5(data):
	m = hashlib.md5()
	m.update(data)
	return m.hexdigest()

def secServer():
	while True:
		message, clientAdrs = serverSocket.recvfrom(MAX_UDP_PAYLOAD)
		dmessage = message.decode()
	 
		# Compute checksum of file
	#	check_su = sys.argv[1]

	#	file_checksum = md5(b"{check_su}")
		
		socket_list = []
	#	socket_list.append(file_checksum)
		
		with open(sys.argv[1], "rb") as f:
			# Read file
			file_data = f.read()
			file_barray = bytearray()
			file_size = sys.getsizeof(file_data)
			file_csum = md5(str(file_size).encode())
			socket_list.append(file_csum)
			sec = 0
			i = 0
			x = sys.getsizeof(file_data)
			if(dmessage == "LIST"):
				while( i < x):
					Slice_n = slice(i,buffersize+1,1)
					file_barray += file_data[Slice_n]				
					b = sys.getsizeof(file_barray)
					i = i + b + 1
					
					section_size = 	b					
					section_size_checksum = md5(str(section_size).encode())
					message = f'{sec} {section_size} {section_size_checksum}'
					socket_list.append(message)
					
					sec = sec + 1
					
				strs = ''.join(socket_list)
				serverSocket.sendto(strs.encode(),clientAdrs)

#MAIN	
secServer()

 	




		
