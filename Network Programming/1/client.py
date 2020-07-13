from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect(("127.0.0.1", 9999))

msg = s.recv(1024)
# we try to receive up to 1024 bytes from the server

s.close()

print(msg.decode('ascii'))
