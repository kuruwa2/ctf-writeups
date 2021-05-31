import socketserver
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from binascii import unhexlify

class Task(socketserver.BaseRequestHandler):

	def recv(self):
		return self.request.recv(1024).strip()

	def send(self, msg):
		self.request.sendall(msg + b'\n')

	def handle(self):
		privkey = RSA.generate(1024)

		n = privkey.n
		e = privkey.e

		self.send(b'Welcome to ReSident evil villAge, sign the name "Ethan Winters" to get the flag.')
		self.send(b'n = ' + str(n).encode())
		self.send(b'e = ' + str(e).encode())

		while True:
			self.request.sendall(b'1) sign\n2) verify\n3) exit\n')
			option = self.recv()

			if option == b'1':
				self.request.sendall(b'Name (in hex): ')
				msg = unhexlify(self.recv())
				if msg == b'Ethan Winters' or bytes_to_long(msg) >= n:  # msg+k*n not allowed
					self.send(b'Nice try!')
				else:
					sig = pow(bytes_to_long(msg), privkey.d, n)     # TODO: Apply hashing first to prevent forgery
					self.send(b'Signature: ' + str(sig).encode())

			elif option == b'2':
				self.request.sendall(b'Signature: ')
				sig = int(self.recv())
				verified = (pow(sig, e, n) == bytes_to_long(b'Ethan Winters'))
				if verified:
					self.send(b'AIS3{THIS_IS_A_FAKE_FLAG}')
				else:
					self.send(b'Well done!')

			else:
				break

class ForkingServer(socketserver.ForkingTCPServer, socketserver.TCPServer):
	pass

if __name__ == "__main__":
	HOST, PORT = '0.0.0.0', 42069
	print(HOST, PORT)
	server = ForkingServer((HOST, PORT), Task)
	server.allow_reuse_address = True
	server.serve_forever()
