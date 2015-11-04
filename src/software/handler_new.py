from hardware.memory import Memory
from software.program import Program
from software.pcb import PCB
from software.pcb_table import PCBTable
from software.process_states import ProcessStates

class HandlerNew:
    
    def __init__(self,pcbTable,hardDisk,memory,qReady):
    
        self.pcbTable = pcbTable
        self.hardDisk = hardDisk
        self.memory = memory
        self.qReady = qReady
        
    #pseudocodigo
    #basicamente es el ProgramLoader
    
    #va a buscar el programa al HD
    #lo carga en memoria
    #lo pone en qReady
    
    def run(self,programName):
        
        print("new handle in action!")
        
        self.handle(programName) 
        
    def handle(self,name):
        self.load(name)
                
    def load(self,programName):
        programCopy = self.hardDisk.find(programName)
        pcb = self.pcbCreate()
        self.memoryDump(programCopy, pcb)
        self.pcbTable.add(pcb)
        self.qReady.queue(pcb)
        
        
    def memoryDump(self, program, pcb):
       
        pcb.baseDirection = self.memory.firstFreeDirection
        
        for n in range(program.programLength()):
            instructionToDump = program.getInstruction(n)
            self.memory.put(instructionToDump)
            
        pcb.lastDirection = self.memory.firstFreeDirection
    
    def pcbCreate(self):
        pcbId = self.pcbTable.nextFreeId()
        return PCB(pcbId)