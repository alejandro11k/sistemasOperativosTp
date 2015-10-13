
from hardware.hardDisk import HardDisk
from hardware.memory import Memory

class ProgramLoader:
    
    def __init__(self,hardDisk,memory):
        self.hardDisk = hardDisk
        self.memory = memory
        self.programCopy = None
    
    def load(self,programName):
        self.programCopy = self.hardDisk.find(programName)
        self.memoryDump(self.programCopy)
        
    def memoryDump(self,program):
        
        
        self.instructionToDump(program.nextInstruction())
        self.memory.put(self.instructionToDump)
