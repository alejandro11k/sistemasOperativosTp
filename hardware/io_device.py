from software.process_states import ProcessStates
from hardware.irq import Irq
from hardware.irq_type import IrqType

class IoDevice:

    def __init__(self, name):
        self.name = name
        self.memory = None
        
        self.pcb = None
        self.instructions = set()
        self.irq = None
        self.qio = None
        
        self.interruptorManager = None


    def setUp(self,interruptorManager,qio,memory):
        
        self.interruptorManager = interruptorManager
        self.qio = qio
        self.memory = memory
    
    def knownInstruction(self,instruction):
        return instruction in self.instructions
    
    def learnInstruction(self,instruction):
        self.instructions.add(instruction)
    
    def fetch(self):
        
        #x = self.qio.emptyQ()
        
        if self.pcb==None and self.qio.emptyQ():
            print("ioDev:idle:",self.name)
        
        else:
            self.setPCB()
            
            #result = self.calculateDirection()
            self.instruction = self.memory.get(self.pcb)
            
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

        
        result = self.instruction.process()
        
        if not(result==None):
                self.irq = Irq(IrqType.irqNEW, result)
                self.interruptorManager.handle(self.irq)
        
        print("IO Dev:procesando instruccion idP:" ,self.name,":",self.pcb.idProcess)
        self.pcb.incrementProgramCounter()
        