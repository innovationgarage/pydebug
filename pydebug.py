import sys
import threading
import code
import socket
import code
import debugthread
import io

foo="xxx"

s = socket.socket(socket.AF_INET)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 4711))
s.listen(0)
while True:
    ss, addr = s.accept()
    stdin =io.TextIOWrapper(ss.makefile('rb', 0), encoding='utf8')
    stdout = io.TextIOWrapper(ss.makefile('wb', 0), encoding='utf8')
    debugthread.shell(stdin, stdout, stdout, locals())
