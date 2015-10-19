#!python
import time
import threading
import math
import Main
from Systems import DT
from Systems import Thrower
from tkinter import *
import sys
##from PySide.QtGui import *


##mapper= {'Drive Train': DT, 'Thrower': Thrower}

def hello():
    print("hello!")

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
##            try:
##                self.function.main()
##                self._stopevent.wait(self._sleepperiod)
##            except KeyboardInterrupt:
##                self.join()
            self.function.main()
            self._stopevent.wait(self._sleepperiod)
        print("%s ends" % (self.getName(),))
    def join(self, timeout=None):
        """ Stop the thread and wait for it to end. """
        self._stopevent.set( )
        threading.Thread.join(self, timeout)

def main():
##    app = QApplication([])
##
##    window = QMainWindow()
##    bar = QMenuBar(window)
##    window.setMenuBar(bar)
##    m = QMenu('menu', bar)
##    bar.addMenu(m)
##    action = QAction('action', m, checkable=True)
##    m.addAction(action)
##
##    window.show()
##    app.exec_()
##    print(action.isChecked())
    root=Tk()
    menubar = Menu(root)
    
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=hello)
    filemenu.add_command(label="Save", command=hello)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # create more pulldown menus
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=hello)
    editmenu.add_command(label="Copy", command=hello)
    editmenu.add_command(label="Paste", command=hello)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=hello)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    root.config(menu=menubar)

if __name__ == "__main__":
    driveTrain = StoppingThread(DT,"DT")
    thrower = StoppingThread(Thrower, "Thrower")
    driveTrain.start()
    thrower.start()
    run=True
    while run:
        try:
            time.sleep(0.01)
            pass
        except:
            driveTrain.join()
            thrower.join()
            Main.end()
            run=False
    
