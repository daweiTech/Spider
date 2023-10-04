num = 100
list_nums = [11,22]

def test1():
    global num#修改这个整形数据num时，要告诉解释器具体哪一个变量
    num = num+1

def test2():
    list_nums.append(33)#这边直接指明肯定是哪一个数组