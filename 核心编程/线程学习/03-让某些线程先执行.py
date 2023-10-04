import time
import threading

def test1():
    print("1")
    time.sleep(1)

def test2():
    print("2")
    time.sleep(1)

def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()#相当于在之前的引用中后面加上小括号，使之成为实例对象
    t2.start()
    print(len(threading.enumerate()))


if __name__ == '__main__':
    main()