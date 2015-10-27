from software.my_queue import MyQueue
from software.pcb import PCB

class QReady():

    def __init__(self):
        self.pcbs = []
        
    def queue(self,pcb):
        self.pcbs.insert(0, pcb)
    
    def getFirst(self):
        pcb = self.pcbs.pop(0)
        return pcb