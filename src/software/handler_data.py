from software.handler_kill import KillHandler
#from software.handler_out import TimeOutHandler
#from software.handler_io import IOHandler
from hardware.irq_type import IrqType

class HandlerData:
    
    '''
    Handler container and IRQ correspondence
    '''
    def __init__(self):
        self.irqDictionary = {}
        self.initialize()
    
    def initialize(self):
        irqType = IrqType.irqKILL
        handler = KillHandler()
        self.irqDictionary[irqType.name] = handler
        
    def getHandler(self,irqType):
        handler = self.irqDictionary[irqType.name]
        return handler
    
    def addHandler(self, iRQtype,irqHandler):
        self.irqDictionary[iRQtype] = irqHandler
