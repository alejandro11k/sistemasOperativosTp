from software.pcb import PCB
from software.q_ready import QReady
from hardware.cpu import CPU
from software.process_states import ProcessStates

class Schedule:
    
    def __init__ (self,qready,cpu):
        self.qready = qready
        self.cpu = cpu
        
    def roundRobinQuantum(self,quantum):
        nextPCB = self.qready.getFirst()
        nextPCB.state = ProcessStates.processRunning
        self.cpu.setPCB(nextPCB,quantum)
        
        