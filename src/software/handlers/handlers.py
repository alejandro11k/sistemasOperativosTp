from hardware.irq_type import IrqType
from software.handlers.handler_io_from_cpu import HandlerIOfromCPU
from software.handlers.handler_io_from_io import HandlerIOfromIO
from software.handlers.handler_kill import HandlerKill
from software.handlers.handler_new import HandlerNew
from software.handlers.handler_new import HandlerNew2
from software.handlers.handler_process import HandlerProcess
from software.handlers.handler_time_out import HandlerTimeOut

class Handlers:
    
    def __init__(self,interruptionManager,cpu,pcbTable,scheduler,qReady,hardDisk,memory):

        self.addIrq(cpu,pcbTable,scheduler,qReady,hardDisk,memory)
        self.registerHandlers(interruptionManager)
        
    def addIrq(self,cpu,pcbTable,scheduler,qReady,hardDisk,memory):
        
        self.handlerKill = HandlerKill(cpu,pcbTable,scheduler)
        self.handlerTimeOut = HandlerTimeOut(cpu,qReady,scheduler)
        self.handlerIOfromCPU = HandlerIOfromCPU(cpu)
        self.handlerIOfromIO = HandlerIOfromIO(qReady)
        self.handlerNew = HandlerNew2(hardDisk,memory,pcbTable,qReady,scheduler,cpu)

    def registerHandlers(self,interruptionManager):
        interruptionManager.register(IrqType.irqKILL, self.handlerKill)
        interruptionManager.register(IrqType.irqTIME_OUT, self.handlerTimeOut)
        interruptionManager.register(IrqType.irqIOfromCPU, self.handlerIOfromCPU)
        interruptionManager.register(IrqType.irqIOfromIO, self.handlerIOfromIO)
        interruptionManager.register(IrqType.irqNEW, self.handlerNew)