#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-8 15:01
 查看一个目录下的文件
"""

import sys
import os


def Main():
    sys.stdout.write("program is started ... \n")
    print os.listdir("d:/")


if __name__ == "__main__":
    Main()

# program is started ...
# ['$RECYCLE.BIN', 'activeMQ', 'Aero 8 Theme', 'antManual', 'apache-ant-1.8.4', 'apache-maven-3.0.4', 'axis-1_4', 'axis2-1.6.2',
# 'beyond', 'demo-project', 'dexpot', 'docs', 'eclipse', 'everedit', 'experiences', 'gitDoc', 'good_books', 'idocdown_v21', 'Java EE Api',
# 'Java SE Api', 'junit', 'kankan', 'Metro X', 'mongodb-win', 'MySQL', 'MySQLDATA', 'opt', 'ppt\xca\xd5\xb2\xd8', 'Program Files',
#  'Program Files (x86)', 'ProgramData', 'Python_v3.0c1_PyTutorial_zh081031', 'qwertick', 'redis-2.4.5', 'redis-latest', 'resin-3.1.12',
#  'scala-2.9.2', 'scala-books', 'share', 'shell-video', 'software', 'SOHU-CNC.pcf', 'SOHU-CTC.pcf', 'spring-framework-reference.pdf',
# 'System Volume Information', 'TDDOWNLOAD', 'tutorial_books', 'Ubuntu02.jpg', 'VanDyke', 'Winscp', 'xfire-1.2.6', 'Youku Files',
#  'zHlhmzq.jpg', 'zooData', 'zooData-mem2', 'zookeeper-3.4.3', 'zookeeper-3.4.3-mem2', '\xcd\xbc\xc6\xac\xca\xd5\xb2\xd8',
# '\xb1\xda\xd6\xbd\xca\xd5\xb2\xd8', '\xc9\xf9\xd2\xf4\xb7\xbd\xb0\xb8', '\xb9\xa4\xbe\xdf\xb0\xfc', '\xd3\xb0\xc6\xac',
# '\xce\xc4\xb5\xb5', '\xcc\xd4\xb1\xa6\xba\xa3\xc1\xbf\xca\xfd\xbe\xdd\xb2\xfa\xc6\xb7\xbc\xbc\xca\xf5\xbc\xdc\xb9\xb9.pptx',
# '\xb0\xd9\xb6\xc8\xd4\xc6', '\xcf\xe0\xc9\xf9', '\xbc\xf2\xc0\xfa', '\xd7\xaa\xd5\xcb']

