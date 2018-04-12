import socket, sys
host, port = sys.argv[1:]

#look up th given data
results = socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM)

#We may get multiple results back. Display each one.
for result in results:
    print "-"*60
    #print whether we got back an IPv4 or IPv6 result.
    if result[0] == socket.AF_INET:
        print "Family: AF_INET"
    elif result[0] == socket.AF_INET6:
        print "Family: AF_INET6"
    else:
        print "Family: result[0]"

    #indicate whether  it's a stream(TCP) or datagram (UDP) result.
    if result[1] == socket.SOCK_STREAM:
        print "Socket Type: SOCK_STREAM"
    elif result[1] == socket.SOCK_DGRAM:
        print "Scket Type: SOCK_DGRAM"

    print "Protocol:", result[2]
    print "Canonical Name:", result[3]
    print "Socket Address:", result[4]
