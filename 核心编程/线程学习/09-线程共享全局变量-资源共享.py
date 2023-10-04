import time
import threading

g_num = 0
def test1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print(f'in test1 g_num={g_num}')

def test2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print(f'in test2 g_num={g_num}')

def main():
    t1 = threading.Thread(target=test1,args=(100000,))
    t2 = threading.Thread(target=test2, args=(100000,))

    t1.start()
    t2.start()

    print(f'in main g_num={g_num}')

if __name__ == '__main__':
    main()


# in test1 g_num=100000
# in main g_num=196810in test2 g_num=200000
# 时间片轮转时，赋值前可能会到另一个进程开始工作，造成可能加了两次值还是1
#这样就引入锁的概念