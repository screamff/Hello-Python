#! python2
import socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

localaddr = ("", 7777)
udp_socket.bind(localaddr)
recv_data = udp_socket.recvfrom(1024)
recv_message = recv_data[0]
send_addr = recv_data[1]

print recv_data
print "from:%s message:%s" % (str(send_addr), recv_message)
udp_socket.close()
