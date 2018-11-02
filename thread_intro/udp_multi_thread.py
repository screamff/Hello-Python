# coding:utf-8
import socket
import threading


def recv_msg(udp_socket):
    # 接受数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print recv_data


def send_msg(udp_socket, dest_ip, dest_port):
    while True:
        # 发送数据
        send_data = raw_input("message:")
        udp_socket.sendto(send_data, (dest_ip, dest_port))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地ip端口
    udp_socket.bind(("", 7080))
    # 对方ip端口
    dest_ip = "127.0.0.1"
    dest_port = 7888
    # 创建线程
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg,
                              args=(udp_socket, dest_ip, dest_port,))
    t_recv.start()
    t_send.start()


if __name__ == "__main__":
    main()
