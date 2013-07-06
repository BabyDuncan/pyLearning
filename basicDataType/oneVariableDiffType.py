#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-8 14:49
 一个变量在程序的不用地方，可以变换成不同的类型。
"""

import sys


def Main():
    sys.stdout.write("program is started... \n")

    i = 1
    print(i, type(i), id(i))

    i = 1000000000000
    print(i, type(i), id(i))

    i = 3.14159
    print(i, type(i), id(i))


if __name__ == "__main__":
    Main()