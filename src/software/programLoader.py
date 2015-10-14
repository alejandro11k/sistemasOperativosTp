from hardware.hardDisk import HardDisk
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
        self.programCopyInitialAdress = None
        self.programCopyLastAdress = None
        self.programCopyPCB = None
        self.qReady = qReady
        
        
    def load(self,programName):
        self.pcbCreate()
        self.programCopy = self.hardDisk.find(programName)
        self.memoryDump(self.programCopy)
        self.programCopyPCB.fillDirections(self.programCopyInitialAdress, self.programCopyLastAdress)
        self.pcbTable.add(self.programCopyPCB)
        self.qReady.queue(self.programCopyPCB)
        self.programCopyPCB.setState(ProcessStates.processReady)
        self.setDefault()
        
        
    def memoryDump(self,program):
        self.programCopyInitialAdress = self.memory.firstFreeDirection
        
        while(not program.isLastInstuction()):
            self.instructionToDump(program.nextInstruction())
            self.memory.put(self.instructionToDump)
            
        self.instructionToDump(program.nextInstruction())
        self.memory.put(self.instructionToDump)
        
        self.programCopyLastAdress = self.memory.lastFreeDirection
    
    def pcbCreate(self):
        self.programCopyPCB = PCB(self.pcbTable.nextFreeId())
        
    def setDefault(self):
        self.programCopyInitialAdress = None
        self.programCopyLastAdress = None
        self.programCopyPCB = None
        
        