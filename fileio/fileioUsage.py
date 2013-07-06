#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-13 19:22
 file 操作
"""


def Main():
    print "start ... \n"
    content = """
        class Hello{
            public static void main(String ... args){
                System.out.println("Hello");
            }
        }
    """

    myfile = file("d:/Hello.java", 'w')
    myfile.write(content)
    myfile.close()

    print "finish .."


if __name__ == "__main__":
    Main()
