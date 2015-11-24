from threading import Thread, RLock
from logging import threading
from time import sleep

class Clock(Thread):
    
    def __init__(self,interruptionManager,cpu,io_dev_1,io_dev_2):
        Thread.__init__(self)
        self.ciclos = 20
        self.cpu = cpu
        self.interruptionManager = interruptionManager
        self.io_dev_1 = io_dev_1
        self.io_dev_2 = io_dev_2
        
    def pulse(self):
        self.cpu.fetch()
        self.interruptionManager.fetch()
        self.io_dev_1.fetch()
        self.io_dev_2.fetch()
        
    def run(self):
        Thread.run(self)
        for x in range(1,self.ciclos):
            self.pulse()
            sleep(1)
            x+=1