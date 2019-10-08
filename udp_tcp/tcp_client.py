# coding:utf-8
import socket


def main():
    # 1.创建套接字
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 目标信息
    server_ip_port = ("127.0.0.1", 3789)
    # 2.连接服务器
    tcp_client.connect(server_ip_port)
    # 3.发送/接收kokl数据
    send_data = input("message:")
    tcp_client.send(send_data.encode('utf-8'))
    # 接受数据
    recvdata = tcp_client.recv(1024)
    print("服务器应答:", recvdata)

    # 4.关闭套接字
    tcp_client.close()


if __name__ == "__main__":
    main()
