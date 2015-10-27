from software.pcb import PCB
from software.q_ready import QReady
from hardware.cpu import CPU

class Schedule:
    
    def __init__ (self,qready,cpu):
        self.qready = qready
        self.cpu = cpu
        
    def roundRobinQuantum(self,quantum):
        nextPCB = self.qready.getFirst()
        self.cpu.setPCB(nextPCB,quantum)
        
        