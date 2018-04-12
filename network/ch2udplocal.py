import socket,sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = raw_input("Input the host:")
textport = raw_input("Input the port number or protocol name:")

try:
    port = int(textport)
except ValueError:
    port = socket.getservbyname(textport, 'udp')

s.connect((host, port))
data = raw_input('Enter data to transmit:')
s.sendall(data)
print 'Looking for replies; press Ctrl-C or Ctrl-Break to stop'

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    print buf
