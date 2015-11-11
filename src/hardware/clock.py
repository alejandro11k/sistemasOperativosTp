from threading import Thread, RLock
from logging import threading
from time import sleep

class Clock(Thread):
    
    def __init__(self,device,interruptionManager):
        Thread.__init__(self)
        self.device = device
        self.interruptionManager = interruptionManager
        
    def pulse(self):
        self.device.fetch()
        self.interruptionManager.fetch()
        
        
    def run(self):
        Thread.run(self)
        for x in range(1,100):
            self.pulse()
            sleep(1)
            x+=1