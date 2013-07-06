#-*- coding: utf-8 -*-
"""
 Author: guohaozhao116008@sohu-inc.com
 Since: 13-6-26 17:33
 Thrift 的客户端
"""
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport
from thrifttest.person import PersonService
from thrifttest.person.ttypes import Person


def Main():
    print "client started ..."

    socket = TSocket.TSocket("localhost", 7913)
    transport = TTransport.TFramedTransport(socket)
    transport.open()
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    service = PersonService.Client(protocol)
    person = Person("BabyDuncan", 21)
    result = service.personToString(person)
    print "result is " + result


if __name__ == "__main__":
    Main()
