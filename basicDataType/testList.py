#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-8 17:33
 py 基本数据类型 list
 list[start:end:step] list 的切片操作
"""


def Main():
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    print array[2]
    array[0] = 99
    print  array
    print "array length is " + str(len(array))
    print array[1:-1:2]


def sort():
    print  "function two is started ..."
    array = [3, 4, 11, 2, 32, 45, 112, 23]
    print array
    array.reverse()
    print  array
    array.sort()
    print  array


if __name__ == "__main__":
    Main()
    sort()