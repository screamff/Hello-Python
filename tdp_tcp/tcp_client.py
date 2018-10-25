import socket


def main():
    # 1.创建套接字
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 目标信息
    server_ip_port = ("127.0.0.1", 8888)

    # 2.连接服务器
    tcp_client.connect(server_ip_port)
    while True:
        # 3.发送/接收数据
        send_data = raw_input("message:")
        # 退出指令
        if send_data == "close" or "quit":
            break
        tcp_client.send(send_data)
        # 接受数据
        recvdata = tcp_client.recv(1024)
        print "服务器应答:", recvdata

    # 4.关闭套接字
    tcp_client.close()


if __name__ == "__main__":
    main()
