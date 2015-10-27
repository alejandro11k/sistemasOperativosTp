#from memory import *
#from pcb import *
from irq import Irq
from irq_type import IrqType

class CPU:

    def __init__(self, memory, interruptorManager):
        self.memory = memory
        self.pcb = None
        self.result = None
        self.instruction = None
        self.interruptorManager = interruptorManager
        self.quantum = 0
        self.irq = None

    def fetch(self):
        self.result = self.calculateDirection()
        self.instruction = self.memory.get(self.result)
        
        # IO?
        # si la instruccion es de IO la que puede ser de IO es la instruccion del programa
        
        if self.instruction.instructionType==InstructionIO:
            pass
            #self.interruptorManager.register(IO_INTERRUPT, new IOHandler())
        else:
            ## si no es de IO la proceso
            ## despues de procesar la instruccion
            self.process()

    def calculateDirection(self):
        self.result = self.pcb.programCounter + self.pcb.baseDirection 
        return self.result

    def setPCB(self,pcb,quantum):

        self.pcb=pcb
        self.quantum = quantum

    def process(self):
        
        #revisa si se consumio los ciclos maximos para un mismo proceso
        if self.quantum==0:
            pass
            #self.interruptorManager.register("TIMEOUT_INTERRUPT", TimeOutHandler())

        #revisa si el programa va a ejecutar su ultima instruccion
        if self.instruction.instructionType==InstructionEND: ## no tiene mas instrucciones
            self.irq = Irq(IrqType.irqKILL,self.pcb)
            self.interruptorManager.handle(self.irq)
        #ejecuta la instruccion
        else:
            self.instruction.process()
            self.pcb.incrementProgramCounter()  
            self.quantum + self.quantum - 1

