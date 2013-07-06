#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-8 14:58
 python 是强类型的，int 和 str 是不可以相加减的
"""

import sys


def Main():
    sys.stdout.write("program is started ... \n")
    i = 10
    s = "ok"
    # print i + s
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    print(str(i) + s)


if __name__ == "__main__":
    Main()
