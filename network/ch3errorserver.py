import socket, traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)
print "Waiting for connections..."

while 1:
    try:
        clientsock, clientaddr = s.accept()
        buf = clientsock.recv(1024)
        if buf:
            clientsock.send("WELCOME TO SERVER")
            print buf
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    try:
        print "Got connection from", clientsock.getpeername(), clientaddr
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

        #close the connection

    # try:
    #     clientsock.close()
    # except KeyboardInterrupt:
    #         raise
    # except:
    #     traceback.print_exc()
