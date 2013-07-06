#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-13 19:32
 py 读取文件
"""


def Main():
    print "start ..."

    f = open("d:/Hello.java")
    i = 0
    while True:
        line = f.readline()
        if line:
            print  line
            i += 1
        else:
            break

    print "i is " + str(i)
    f.close()
    print "end ..."


if __name__ == "__main__":
    Main()