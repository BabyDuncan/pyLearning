#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-9 14:26
 py 中的字典  相当于java 中set
"""


def Main():
    mydict = {"key": "value", "foo": "bar"}
    print  mydict
    #   增加一个字段
    mydict["haha"] = "heihei"
    print  mydict
    #     删除一个字段
    del (mydict["key"])
    print  mydict
    #     修改一个字段
    mydict["foo"] = "newBar"
    print  mydict
    #     查看一个字段
    print mydict["haha"]

    # 遍历
    for k in mydict:
        print("mydict[%s] is " % k, mydict[k])

    #         key set and value set
    print mydict.keys()
    print mydict.values()

    #  has key ?
    if mydict.has_key("foo"):
        print "has foo"
        print mydict["foo"]
    else:
        print "no foo"


if __name__ == "__main__":
    Main()
