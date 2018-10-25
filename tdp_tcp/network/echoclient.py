import socket, sys
port = 51423
host = 'localhost'

data = "x" * 1024  #1kB of data
# data = "x" * 10485760  #10MB of data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

bytewritten = 0
while bytewritten < len(data):
    startpos = bytewritten
    endpos = min(bytewritten + 1024, len(data))
    bytewritten += s.send(data[startpos:endpos])
    print "Wrote %d bytes\n" % bytewritten

s.shutdown(1) #need to find out

print "All data sent."
while 1:
    buf = s.recv(1024)
    if not len(buf):
        break
    print buf
