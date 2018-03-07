#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(('192.168.3.168',60001))
L = ['M','A','P']
data = [chr(255) for i in range(360000)]
L.extend(data)
msg = "".join(L)
while True:
    s.send(msg)
s.send('exit')
s.close()
