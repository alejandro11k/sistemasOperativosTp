from software.my_queue import MyQueue
from software.pcb import PCB
from hardware.irq import Irq
from hardware.irq_type import IrqType

class QReady():

    def __init__(self):
        self.pcbs = []
        
    def queue(self,pcb):
        self.pcbs.append(pcb)
        
    def getFirst(self):
        #empty pcbs broke
        if len(self.pcbs) < 0:
            pcb = self.pcbs.pop(0)
            return pcb
    
    