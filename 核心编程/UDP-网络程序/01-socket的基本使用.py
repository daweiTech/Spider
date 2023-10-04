# -*- coding: utf-8 -*-
# @Time    : 2022/7/15 16:43
# @Author  : 4v1d
# @File    : 01-socket的基本使用.py
# @Software: PyCharm

import socket

def main():

    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    udp_socket.sendto(b'haha',('192.168.204.128',8080))

    udp_socket.close()

if __name__ == '__main__':
    main()