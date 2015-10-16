#!python
import time
import threading
import math
import Main
from Systems import DT
from Systems import Thrower

##mapper= {'Drive Train': DT, 'Thrower': Thrower}

class StoppingThread(threading.Thread):
    def __init__(self, function="Main", name='TestThread'):
        """ constructor, setting initial variables """
        self._stopevent = threading.Event()
        self._sleepperiod = 0.001
        self.function=function
        threading.Thread.__init__(self, name=name)
    def run(self):
        print("TestThread begins")
        """ main control loop """
        while not self._stopevent.isSet():
            self.function.main()
            self._stopevent.wait(self._sleepperiod)
        print("%s ends" % (self.getName(),))
    def join(self, timeout=None):
        """ Stop the thread and wait for it to end. """
        self._stopevent.set( )
        threading.Thread.join(self, timeout)

if __name__ == "__main__":
    driveTrain = StoppingThread(DT,"DT")
    thrower = StoppingThread(Thrower, "Thrower") 
    driveTrain.start()
    thrower.start()
    run=True
    while run:
        try:
            pass
        except:
            driveTrain.join()
            thrower.join()
            Main.end()
            run=False
    
