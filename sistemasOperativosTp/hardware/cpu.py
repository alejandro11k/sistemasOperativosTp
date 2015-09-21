#from memory import *
#from pcb import *

class CPU:

    def __init__(self, memory, interruptorManager):
        self.memory = memory
        self.pcb = None
        self.result = None
        self.instruction = None
        self.interruptorManager = interruptorManager
        self.timeOutLimit = 5
        self.programCounter = 0

    def fetch(self):
        self.result = self.calculateDirection()
        self.instruction = self.memory.get(self.result)
        # IO?
        self.pcb.incrementPC()
        self.incrementPC()

    def calculateDirection(self):
        self.result = self.pcb.programCounter + self.pcb.baseDirection 
        return self.result

    def setPCB(self,pcb):

        self.pcb=pcb
        # si el pcb es de IO la que puede ser de IO es la instruccion del programa
        # self.interruptorManager.register(IO_INTERRUPT, new IOHandler())
        self.fetch()

    def incrementPC(self):

        self.programCounter = self.programCounter + 1
        self.pcb.programCounter + self.programCounter
        
        self.timeOutLimit + self.timeOutLimit - 1
        
        #revisa si el programa termino
        if (self.pcb.instructions==self.pcb.programCounter): ## no tiene mas instrucciones
            self.programCounter=0
            #self.interruptorManager.handle(new irq(self.pcb, "kill_insterrupt"))
        
        #revisa si se consumio los ciclos maximos para un mismo proceso
        if (self.timeOutLimit==1): 
            self.programCounter=0
            #self.interruptorManager.register("TIMEOUT_INTERRUPT", TimeOutHandler())
          
        #prosigue con la proxima instruccion, si no se lanzo alguna interrupcion  
        if (self.programCounter!=0):
            self.fetch()



