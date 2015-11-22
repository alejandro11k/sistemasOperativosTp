from software.process_states import ProcessStates
from hardware.irq import Irq
from hardware.irq_type import IrqType

class IoDevice:

    def __init__(self, name, memory):
        self.name = name
        self.memory = memory
        
        self.pcb = None
        self.instructions = set()
        self.irq = None
        self.qio = None
        
        self.interruptorManager = None


    def setUp(self,interruptorManager,qio):
        
        self.interruptorManager = interruptorManager
        self.qio = qio
    
    def knownInstruction(self,instruction):
        return instruction in self.instructions
    
    def learnInstruction(self,instruction):
        self.instructions.add(instruction)
    
    def fetch(self):
        
        x = self.qio.emptyQ()
        x
        
        if self.pcb==None and self.qio.emptyQ():
            print("ioDev:idle")
        
        else:
            self.setPCB()
            
            result = self.calculateDirection()
            self.instruction = self.memory.get(result)
            
            self.process()
            
            self.irq = Irq(IrqType.irqIOfromIO,self.pcb)
            self.interruptorManager.handle(self.irq)
            self.pcb=None

    def calculateDirection(self):
        result = self.pcb.programCounter + self.pcb.baseDirection 
        return result

    def setPCB(self):

        nextPCB = self.qio.getFirst()
        nextPCB.state = ProcessStates.processRunning
        
        self.pcb = nextPCB
        
        
    def process(self):

        self.instruction.process()
        print("IO Dev:procesando instruccion idP:" ,self.pcb.idProcess)
        self.pcb.incrementProgramCounter()
        