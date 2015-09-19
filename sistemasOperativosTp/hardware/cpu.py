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
        self.PC = 0

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

        self.PC = self.PC + 1
        if (self.pcb.instrutions==0): ## no tiene mas instrucciones
            self.PC=0
            #self.interruptorManager.handle(new irq(self.pcb, "kill_insterrupt"))
        if (self.instrutions==self.timeOutLimit): 
            self.PC=0
            #self.interruptorManager.register("TIMEOUT_INTERRUPT", TimeOutHandler())



