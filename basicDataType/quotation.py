#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-8 15:14
 py中的单引号，双引号以及三引号
"""
import sys


def Main():
    sys.stdout.write("program is started ... \n")

    s1 = "  单引号 ' haha' "
    s2 = '  双引号 “xixi”'
    s3 = """

        窗前明月光</br>
        疑是地上霜《》
        举头望明月{}{}
        低头思故乡 ///\\\ ^_^

     """

    print  s1
    print s2
    print s3


if __name__ == "__main__":
    Main()