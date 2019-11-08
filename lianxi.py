# @author : 'CBC'
# @Time   : 2019-11-08
# @File   : lianxi.py


from past.builtins import raw_input

count = 5


def my_fun():
    global count
    count = 10
    print(count)


def fun1():
    print('fun1正在被调用')

    def fun1_inner():
        print('fun1_inner正在被调用')
    fun1_inner()


# fun1()


if __name__ == '__main__':
    # while True:

            print('输入内容：')
            s = raw_input()

            # a, b = s.split(" ")
            # print(int(a) + int(b))
            print(s + '，你好！')