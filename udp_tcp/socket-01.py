#! python2
# coding:utf-8
import socket

# 创建socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 传输信息
message = raw_input("message:")
# 目标ip,端口
des_addr = ("127.0.0.1", 7777)
# 发送信息
udp_socket.sendto(message.encode("utf-8"), des_addr)
# 关闭套接字
udp_socket.close()
