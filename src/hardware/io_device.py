from software.process_states import ProcessStates
from irq import Irq
from irq_type import IrqType

class IoDevice:

    def __init__(self, memory):
        self.memory = memory
        
        self.pcb = None
        self.instruction = None
        self.irq = None
        self.qio = None
        
        self.interruptorManager = None

    def setUp(self,interruptorManager,qio):
        
        self.interruptorManager = interruptorManager
        self.qio = qio
        
    def fetch(self):
        
        if self.pcb==None:
            print("ioDev:idle")
        
        else:
            
            result = self.calculateDirection()
            self.instruction = self.memory.get(result)
            
            self.process()
            
            self.irq = Irq(IrqType.irqIO,self.pcb)
            self.interruptorManager.handle(self.irq)

    def calculateDirection(self):
        result = self.pcb.programCounter + self.pcb.baseDirection 
        return result

    def setPCB(self):

        nextPCB = self.qio.getFirst()
        nextPCB.state = ProcessStates.processRunningIO
        
        self.pcb = nextPCB
        
        
    def process(self):

        self.instruction.process()
        print("IO Dev:procesando instruccion")
        self.pcb.incrementProgramCounter()
        