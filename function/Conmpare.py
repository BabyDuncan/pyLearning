#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-13 17:15
 py 中的比较大小
"""
import random


def compare(x, y):
    if x > y:
        print "yes"
    elif x == y:
        print "equals"
    else:
        print "no"


if __name__ == "__main__":
    x = random.randrange(1, 10)
    y = random.randrange(2, 20)

    print "x is " + str(x)
    print "y is " + str(y)
    compare(x, y)