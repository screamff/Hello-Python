import socket


def main():
    # 1.创建套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定本地信息
    local_addr = ("", 8888)
    tcp_server.bind(local_addr)
    tcp_server.listen(1)
    while True:
        # 等待客户端的连接accept
        print "waiting for connection..."
        new_client_socket, client_addr = tcp_server.accept()
        print "connected!"
        # 接受数据
        recv_data = new_client_socket.recv(1024)
        # 回传数据
        new_client_socket.send("Hellow")
        print recv_data
        new_client_socket.close()
    tcp_server.close()


if __name__ == "__main__":
    main()
