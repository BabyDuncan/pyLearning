#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-13 16:58
 py读取一个文件，然后打印文件内容
"""


def Main():
    f = open("d:/diff")

    s = f.readline()
    print  s


if __name__ == "__main__":
    Main()