import threading

g_num = 100
def test1():
    global g_num
    g_num+=1
    print(f'in test1 g_num={g_num}')

def test2():
    print(f'in test2 g_num={g_num}')

def main():
    t1 = threading.Thread(target=test1)#此时t1，t2都不是线程
    t2 = threading.Thread(target=test2)#两个子线程同时访问全局变量了，一个改一个读
    t1.start()
    t2.start()
    print(f'in main g_num={g_num}')

main()