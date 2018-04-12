import socket
print "Creating socket"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Done"

port = 51423

print "Connecting to remote host on port %d.." % port
s.connect(("127.0.0.1", port))
print "DONE"

print "connected from", s.getsockname()
print "conneted to", s.getpeername()

s.send("hhhhllll")
# print s.recv(1024)
