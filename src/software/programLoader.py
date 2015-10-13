
from hardware.hardDisk import HardDisk
from hardware.memory import Memory
from software.program import Program

class ProgramLoader:
    
    def __init__(self,hardDisk,memory):
        self.hardDisk = hardDisk
        self.memory = memory
        self.programCopy = None
    
    def load(self,programName):
        self.programCopy = self.hardDisk.find(programName)
        #crear el pcb
        
        self.memoryDump(self.programCopy)
        
        
    def memoryDump(self,program):
        
        while(not (program.isLastInstuction())):
            self.instructionToDump(program.nextInstruction())
            self.memory.put(self.instructionToDump)
            
        self.instructionToDump(program.nextInstruction())
        self.memory.put(self.instructionToDump)
    