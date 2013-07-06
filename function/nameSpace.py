#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-13 17:45
 py 中的locals（）函数以及 globals（）函数
"""


def test(ars):
    x = 1
    print locals()


if __name__ == "__main__":
    test(5)
    test("123")
    print globals()
