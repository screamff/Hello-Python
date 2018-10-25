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
        while True:
            # 接受数据
            recv_data = new_client_socket.recv(1024)
            print recv_data
            # 如果recv解堵塞，有两种方式：
            # 1.对方发送了数据
            # 2.对方close了套接字
            if recv_data:
                # 回传数据
                new_client_socket.send("Hellow")
            else:
                break
        new_client_socket.close()
        print "此客户端已关闭"
    tcp_server.close()


if __name__ == "__main__":
    main()
