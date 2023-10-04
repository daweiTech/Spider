# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 9:03
# @Author  : 4v1d
# @File    : 1111111111.py
# @Software: PyCharm
import execjs

# 将js函数以python字符串的类型保存到变量当中
js_str = '''
    function add(x, y){
        return x + y;
        }
'''

# 调用execjs库中的compile指令，括号中设置的是字符串类型的js代码
test = execjs.compile(js_str)

# call 即调用js函数，add为js_str中的函数名，1，2为所需要的参数。
result = test.call('add', 1, 2)
print(result)