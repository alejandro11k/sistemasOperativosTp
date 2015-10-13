
from hardware.hardDisk import HardDisk
from hardware.memory import Memory
from software.program import Program
from software.pcb import PCB

class ProgramLoader:
    
    def __init__(self,hardDisk,memory):
        self.hardDisk = hardDisk
        self.memory = memory
        self.programCopyInitialAdress = None
        self.programCopyLastAdress = None
        self.programCopyPCB = None
        
        
    def load(self,programName):
        self.programCopy = self.hardDisk.find(programName)
        self.memoryDump(self.programCopy)
        self.pcbCreate()
        #crear el pcb
        
    def memoryDump(self,program):
        
        self.programCopyInitialAdress = self.memory.firstFreeDirection
        
        while(not (program.isLastInstuction())):
            self.instructionToDump(program.nextInstruction())
            self.memory.put(self.instructionToDump)
            
        self.instructionToDump(program.nextInstruction())
        self.memory.put(self.instructionToDump)
        
        self.programCopyLastAdress = self.memory.lastFreeDirection
    
    def pcbCreate(self):
        
        self.programCopyPCB = PCB(self.programCopyInitialAdress,self.programCopyLastAdress)
        
        