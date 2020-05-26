# @author : 'CBC'
# @Time   : 2019-11-08
# @File   : lianxi.py
import sys


count = 9


def my_fun(parameter):
    if parameter.__len__() == 1:
        parameter = 'World'
        # print('World', end='')
        return parameter
    else:
        return parameter[1]


def fun1():
    print('fun1正在被调用')

    def fun1_inner():
        print('fun1_inner正在被调用')
    fun1_inner()


# fun1()


if __name__ == '__main__':
    # while True:

        # print('输入内容：')
        # s = raw_input()

        # a, b = s.split(" ")
        # print(int(a) + int(b))
    s = my_fun(sys.argv)
    print(s + '，你好！')
