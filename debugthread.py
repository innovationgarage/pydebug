import sys
import threading
import code

stderr = sys.stderr

class ThreadStd(object):
    def __init__(self, name):
        object.__setattr__(self, '_thread_name', name)
        object.__setattr__(self, '_thread_default', getattr(sys, name))
        setattr(sys, name, self)

    def _thread_file(self):
        return getattr(sys.thread_std, self._thread_name, self._thread_default)
    
    def __getattr__(self, name):
        return getattr(self._thread_file(), name)

    def __setattr__(self, name, value):
        setattr(self._thread_file(), name, value)
    
sys.thread_std = threading.local()
ThreadStd('stdin')
ThreadStd('stdout')
ThreadStd('stderr')

def shell(file, local=None):
    def shell():
        sys.thread_std.stdout = file
        sys.thread_std.stdin = file
        sys.thread_std.stderr = file
        code.interact(local=local)
    threading.Thread(target=shell).run()
    
    
