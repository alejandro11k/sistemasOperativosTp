from hardware.irq import Irq
from hardware.irq_type import IrqType
from software.instruction_type import InstructionType
from software.instruction import Instruction

class CPU:

    def __init__(self, memory):
        self.memory = memory
        
        self.pcb = None
        self.instruction = None
        self.irq = None
        
        self.quantum = 0
        
        self.interruptorManager = None

    def setUp(self,interruptorManager):
        
        self.interruptorManager = interruptorManager
        
    def fetch(self):
        
        # tengo que revisar si hay pcb!
        #if self.pcb==None:
        
        #revisa si se consumio los ciclos maximos para un mismo proceso
        # si el quantum es 0 es porque no hay ningun pcb cargado!
        
        if self.quantum==0:
            if self.pcb==None:
                print("CPU:idle")
            else:
                #self.interruptorManager.register("TIMEOUT_INTERRUPT", TimeOutHandler())
                self.irq = Irq(IrqType.irqTIME_OUT,self.pcb)
                self.interruptorManager.handle(self.irq)
                
        else:
            
            result = self.calculateDirection()
            self.instruction = self.memory.get(result)
            
            # IO?
            # si la instruccion es de IO la que puede ser de IO es la instruccion del programa
            
            if self.instruction.instructionType==InstructionType.instructionIO:
                self.irq = Irq(IrqType.irqIOfromCPU,self.pcb)
                self.interruptorManager.handle(self.irq)
                #self.interruptorManager.register(IO_INTERRUPT, new IOHandler())
            else:
                ## si no es de IO la proceso
                ## despues de procesar la instruccion
                self.process()

    def calculateDirection(self):
        result = self.pcb.programCounter + self.pcb.baseDirection 
        return result

    def setPCB(self,pcb,quantum):

        self.pcb=pcb
        self.quantum = quantum

    def process(self):

        #revisa si el programa va a ejecutar su ultima instruccion
        if self.instruction.instructionType==InstructionType.instructionEND: ## no tiene mas instrucciones
            self.irq = Irq(IrqType.irqKILL,self.pcb)
            self.interruptorManager.handle(self.irq)
        #ejecuta la instruccion
        else:
            self.instruction.process()
            print("CPU:procesando instruccion")
            self.pcb.incrementProgramCounter()  
            self.quantum = self.quantum - 1
    
    def isIdle(self):
        retValue=False
        if self.pcb==None:
                print("CPU:idle")
                retValue=True
        return retValue
