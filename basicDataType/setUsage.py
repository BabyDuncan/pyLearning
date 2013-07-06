#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-13 16:36
 py中的set的使用方法
"""


def Main():
    l = ["a", "b", "c"]
    myset = set(l)
    print  myset
    l2 = ["a", "b", "d"]
    myset2 = set(l2)
    print  myset & myset2


if __name__ == "__main__":
    Main()
