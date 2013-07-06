#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-8 15:20
 使用global 关键字
"""


def Main():
    print s


def list():
    global s
    s = "zifuchuan"


list()
Main()