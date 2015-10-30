from hardware.hard_disk import HardDisk
from hardware.memory import Memory
from software.program import Program
from software.pcb import PCB
from software.pcb_table import PCBTable
from software.process_states import ProcessStates

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
    
        '''while(not program.isLastInstuction()):
            
            instructionToDump = program.nextInstruction()
            self.memory.put(instructionToDump)
        
        instructionToDump = program.nextInstruction()
        self.memory.put(instructionToDump)'''
        
        for n in range(program.programLength()):
            instructionToDump = program.getInstruction(n)
            self.memory.put(instructionToDump)
            
        pcb.lastDirection = self.memory.firstFreeDirection
    
    def pcbCreate(self):
        return PCB(self.pcbTable.nextFreeId())
        
        