import threading
import time
import socket

def is_odd_parity(n=None):
	"""Return True if parity is odd

	Input is hex number as a string
	"""
	n=int(n,16)
	c = 0
	while n:
		c += 1
		n &= n - 1
	if c%2: 
		return True
	else:
		return False

def handle(data=None):
	"""Handler for application B
	"""
	try:
		data = data.split(" ")
		reply = ""

		for n in data:
			if is_odd_parity(n=n): 
				reply += "{0} ".format(n)

		return reply.strip()

	except:
		return "exception raised"


# ip and port dict for appA and appB 
send_to_B = {"ip": "localhost","port": 65520}
send_to_A = {"ip": "localhost","port": 65521}

def send(ip=None, port=0, data=None):
	"""Send data over a socket to the given ip and port

	Input is the ip, port and the data to be sent
	"""
	sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

	sock.sendto(data, (ip, port))

	return True

def receive(ip=None, port=0):
	"""receive data over a socket with given ip and port

	Input is the ip and port to listen to
	"""
	sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

	sock.bind((ip, port))

	while True:
		data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
		if len(data) > 0:
			break

	return data

def applicationA(data=None):
	"""This will imitate the function of Application A, it sends the data
	to application B over a socket communication and it will print data 
	received from application B

	Input is data received from the system
	"""
	send(send_to_B['ip'], send_to_B['port'], data=data)

	print receive(send_to_A['ip'], send_to_A['port'])

def applicationB(data=None):
	"""This will imitate the function of Application B, it listen for data
	from application A and returns a string containing all 32 bit data 
	which has correct odd parity
	"""
	data = receive(send_to_B['ip'], send_to_B['port'])

	data = handle(data)

	time.sleep(2)
	send(send_to_A['ip'], send_to_A['port'], data=data)

def challengeC(N=None):
	try:
		appA = threading.Thread(target=applicationA, args=(raw_input().strip(),) )
		appB = threading.Thread(target=applicationB, args=() )

		appB.start()
		time.sleep(1)
		appA.start()

	except:
		print "Error: unable to start thread"
		exit(1)

if __name__ == "__main__":
	challengeC()
