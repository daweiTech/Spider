import time
import threading

g_num = 0
mutex = threading.Lock()  # 创建互斥锁


def test1(num):
    global g_num
     # 加锁，上锁操作，多线程一般用作IO读写
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print(f'in test1 g_num={g_num}')


def test2(num):
    global g_num

    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print(f'in test2 g_num={g_num}')


def main():
    t1 = threading.Thread(target=test1, args=(100000,))
    t2 = threading.Thread(target=test2, args=(100000,))

    t1.start()
    t2.start()

    time.sleep(1)
    print(f'in main g_num={g_num}')


if __name__ == '__main__':
    main()
