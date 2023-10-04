import time
import threading

g_nums = [11,22]

def test1(temp):
    temp.append(33)
    print(f'in test1 g_nums={temp}')

def test2(temp):
    print(f'in test2 g_nums={temp}')

def main():
    t1 = threading.Thread(target=test1,args=(g_nums,))#这里把数组变成11，22，33
    t2 = threading.Thread(target=test2,args=(g_nums,))#这里传入的已经是[11,22,33]
                                                      #args要求传递元组，加逗号才是元组
    t1.start()
    time.sleep(1)
    t2.start()

    print(f'in main  g_nums={g_nums}')

if __name__ == '__main__':
    main()