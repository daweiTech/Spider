# -*- coding: utf-8 -*-
# @Time    : 2022/7/15 17:08
# @Author  : 4v1d
# @File    : 04-绑定端口来传输数据.py
# @Software: PyCharm
import socket

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localhost_address = ('', 7788)
    udp_socket.bind(localhost_address)

    recv_data = udp_socket.recvfrom(1024)

    print(recv_data)

    udp_socket.close()

if __name__ == '__main__':
    main()