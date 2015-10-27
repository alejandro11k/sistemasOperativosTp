from software.my_queue import MyQueue
from software.pcb import PCB

class QReady():

    def __init__(self):
        self.pcbs = []
        
    def queue(self,pcb):
        self.pcbs = pcb
    
    def getFirst(self):
        return self.pcbs.pop()