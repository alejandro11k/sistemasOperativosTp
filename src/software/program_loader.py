from hardware.hard_disk import HardDisk
from hardware.memory import Memory
from software.program import Program
from software.pcb import PCB
from software.pcbTable import PCBTable
from software.processStates import ProcessStates

class ProgramLoader:
    
    def __init__(self,hardDisk, memory, pcbTable, qReady):
        self.pcbTable = pcbTable
        self.hardDisk = hardDisk
        self.memory = memory
        self.qReady = qReady
        
        
    def load(self,programName):
        programCopy = self.hardDisk.find(programName)
        pcb = self.pcbCreate()
        self.memoryDump(programCopy, pcb)
        self.pcbTable.add(pcb)
        self.qReady.queue(pcb)
        
        
    def memoryDump(self, program, pcb):
        pcb.baseDirection = self.memory.firstFreeDirection
        
        while(not program.isLastInstuction()):
            self.instructionToDump(program.nextInstruction())
            self.memory.put(self.instructionToDump)
            
        self.instructionToDump(program.nextInstruction())
        self.memory.put(self.instructionToDump)
        
        pcb.lastDirection = self.memory.lastFreeDirection
    
    def pcbCreate(self):
        return PCB(self.pcbTable.nextFreeId())
        
        