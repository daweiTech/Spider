# -*- coding: utf-8 -*-
# @Time    : 2022/7/15 16:49
# @Author  : 4v1d
# @File    : 02-发送任意数据到ubuntu的调试助手.py
# @Software: PyCharm

import socket

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    send_data = input('请输入你要发送的数据: ')
    udp_socket.sendto(send_data.encode(),('192.168.204.128',8080))#采用系统默认编码
    udp_socket.close()

if __name__ == '__main__':
    main()