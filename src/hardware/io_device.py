from software.process_states import ProcessStates

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
        