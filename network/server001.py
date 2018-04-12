import socket, traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)
print "Waiting for connections..."
clientsock, clientaddr = s.accept()
try:
    print "Got connection from", clientaddr
except (KeyboardInterrupt, SystemExit):
    raise
except:
    traceback.print_exc()
while 1:
    try:
        buf = clientsock.recv(1024)
        print buf
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
