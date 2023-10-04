import  time
import threading

def test1():
    for i in range(5):
        print("test1")

def main():
    print(threading.enumerate())
    t1 = threading.Thread(target=test1())#现在只是对象，只创建了一个线程对象
    print(threading.enumerate())
    t1.start()                           #此时才成为线程
    print(threading.enumerate())

if __name__ == '__main__':
    main()