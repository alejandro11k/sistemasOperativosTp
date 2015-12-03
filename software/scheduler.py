from software.pcb import PCB
from software.q_ready import QReady
from hardware.cpu import CPU
from software.process_states import ProcessStates

class Schedule:
    
    def __init__ (self,qready,cpu,quantum):
        self.qReady = qready
        self.cpu = cpu
        self.quantum = quantum
        
    
    def giveOne(self):
        self.__roundRobinQuantum(self.quantum)
    
    def __roundRobinQuantum(self,quantum):
        
        if self.qReady.isSomeoneReady():
            nextPCB = self.qReady.getFirst()
            nextPCB.state = ProcessStates.processRunning
            self.cpu.setPCB(nextPCB,quantum)
        
        