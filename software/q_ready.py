from software.my_queue import MyQueue
from software.pcb import PCB
from hardware.irq import Irq
from hardware.irq_type import IrqType

class QReady():

    def __init__(self):
        self.pcbs = []
        self.ready = 0
        
    def queue(self,pcb):
        self.pcbs.append(pcb)
        self.ready+=1
        
    def getFirst(self):
        #empty pcbs broke
        pcb = self.pcbs.pop(0)
        self.ready-=1
        return pcb
    
    def isSomeoneReady(self):
        value = not (self.ready==0)
        return value