# -*- coding=utf-8 -*-

import socket

Address = '0.0.0.1'
Port = 8081

# 服务端
sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockObj.bind((Address, Port))
sockObj.listen(1)
while True:
    conn, address = sockObj.accept()
    data = conn.recv(3000)
    print u'接受到数据为:%s' % data
    conn.close()

# 客户端
Address1 = '127.0.0.1'
sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockObj.connect(Address1, Port)
data1 = 'ssss'
print u'发送数据为:%s' % data
sockObj.send(data1.encode('utf-8'))
sockObj.close()
