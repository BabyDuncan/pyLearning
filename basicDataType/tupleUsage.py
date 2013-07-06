#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-9 14:54
 py 中的元组  数据结构
"""


def Main():
    print "start... \n"
    mytuple = ("a", "b", 1, 2, 3)
    print  mytuple

    mytuple = ((1, 2), (3, 4))
    print  mytuple
    print  mytuple[1][1]
    # tuple 的 解包功能
    a, b = mytuple
    print  a, b


if __name__ == "__main__":
    Main()