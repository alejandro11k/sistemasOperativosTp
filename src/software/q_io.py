from software.my_queue import MyQueue
from software.pcb import PCB

class QIo():

    def __init__(self):
        self.pcbs = []
        
    def queue(self,pcb):
        self.pcbs.append(pcb)
    
    def getFirst(self):
        #empty pcbs broke
        pcb = self.pcbs.pop(0)
        return pcb