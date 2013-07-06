#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-13 17:08
 一个py的九九乘法表
"""


def Main():
    s = [(x, y, x * y) for x in range(1, 10) for y in range(1, 10) if ( x > y)]

    print s


if __name__ == "__main__":
    Main()
