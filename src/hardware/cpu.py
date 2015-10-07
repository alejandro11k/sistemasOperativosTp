#from memory import *
#from pcb import *
from hardware.irq import Irq
from hardware.irqType import IrqType

class CPU:

    def __init__(self, memory, interruptorManager):
        self.memory = memory
        self.pcb = None
        self.result = None
        self.instruction = None
        self.interruptorManager = interruptorManager
        self.timeOutLimit = 5
        self.irq = None

    def fetch(self):
        self.result = self.calculateDirection()
        self.instruction = self.memory.get(self.result)
        # IO?
        
        # si la instruccion es de IO la que puede ser de IO es la instruccion del programa
        # self.interruptorManager.register(IO_INTERRUPT, new IOHandler())
        
        ## si no es de IO la proceso
        
        ## despues de procesar la instruccion
        self.pcb.incrementPC()
        
        self.incrementPC()

    def calculateDirection(self):
        self.result = self.pcb.programCounter + self.pcb.baseDirection 
        return self.result

    def setPCB(self,pcb):

        self.pcb=pcb

    def incrementPC(self):

        self.programCounter = self.pcb.programCounter      
        self.timeOutLimit + self.timeOutLimit - 1
        
        #revisa si el programa termino
        if (self.pcb.instructions==self.pcb.programCounter): ## no tiene mas instrucciones
            self.programCounter=0
            self.irq = Irq(IrqType.irqKILL,self.pcb)
            self.interruptorManager.handle(self.irq)
        
        #revisa si se consumio los ciclos maximos para un mismo proceso
        if (self.timeOutLimit==1): 
            self.programCounter=0
            #self.interruptorManager.register("TIMEOUT_INTERRUPT", TimeOutHandler())
          
        #prosigue con la proxima instruccion, si no se lanzo alguna interrupcion  
        if (self.programCounter!=0):
            self.fetch() ## esto lo hace otrho componente



