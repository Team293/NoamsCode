import time
import threading
import math

def mainCode():
    print(math.pi)
def endCode():
    print("Doneruny")

class TestThread(threading.Thread):
    def __init__(self, name='TestThread'):
        """ constructor, setting initial variables """
        self._stopevent = threading.Event()
        self._sleepperiod = 0.001
        threading.Thread.__init__(self, name=name)
    def run(self):
        print("TestThread begins")
        """ main control loop """
        while not self._stopevent.isSet():
            mainCode()
            self._stopevent.wait(self._sleepperiod)
        print("%s ends" % (self.getName(),))
    def join(self, timeout=None):
        """ Stop the thread and wait for it to end. """
        self._stopevent.set( )
        threading.Thread.join(self, timeout)

if __name__ == "__main__":
    testthread = TestThread()
    testthread.start()
    run=True
    while run:
        try:
            pass
        except:
            testthread.join()
            endCode()
            run=False
    
