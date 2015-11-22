from hardware.memory import Memory
from software.programs_components.program import Program
from software.pcb import PCB
from software.pcb_table import PCBTable
from software.process_states import ProcessStates
from hardware.irq import Irq
from hardware.irq_type import IrqType
from sched import scheduler

class HandlerNew:
    
    def __init__(self,hardDisk, memory, pcbTable, qReady, scheduler,cpu):
        self.pcbTable = pcbTable
        self.hardDisk = hardDisk
        self.memory = memory
        self.qReady = qReady
        self.scheduler = scheduler
        self.cpu = cpu
        
        
    def run(self,irq):
        self.handle(irq.pcb)
        
    def handle(self,programName):
        #lo demas handlers reciven por defecto un pcb
        #pero new recibe un pcb para mantener la creacion
        #del mismo dentro de una interrupcion
        
        print("new handle in action!")
        self.load(programName)
        
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
        
    def printPcbTable(self):
        self.pcbTable.printPcbTable()
        