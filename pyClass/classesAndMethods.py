#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-13 17:58
 带有方法的类
"""


class MyClass:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printme(self):
        print "my name is " + self.name

    @staticmethod
    def hello():
        print "I am static"


if __name__ == "__main__":
    a = MyClass("parker", 30)
    a.printme()
    MyClass.hello()


