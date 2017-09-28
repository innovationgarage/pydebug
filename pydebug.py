import sys
import threading
import code
import socket
import code
import debugthread

foo="xxx"

s = socket.socket(socket.AF_INET)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 4711))
s.listen(0)
while True:
    ss, addr = s.accept()
    f = ss.makefile('r+', 0)
    debugthread.shell(f, locals())
