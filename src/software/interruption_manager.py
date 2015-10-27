from software.kill_handler import KillHandler
from hardware.irq_type import IrqType

class InterruptionManager:
    
    def __init__(self):
        self.irqDictionary = {}
        self.handler = None
        self.fillDictionary()
        
    def fillDictionary(self):
        irqType = IrqType.irqKILL
        handler = KillHandler()
        self.addIrqDictionary(irqType.name, handler)
        
    def addIrqDictionary(self, iRQtype,irqHandler):
        self.irqDictionary[iRQtype] = irqHandler

    def handle(self, irq):
        
        #buscar en el diccionario el handler correspondiente
        self.handler = self.irqDictionary[irq.typeOfIrq.name]
        
        #aca se ejecuta el handle encontrado run
        self.register(irq,self.handler)
    
    def register(self,irq, handler):

        handler.run(irq)
        

"""
KILL_INTERRUPT="#KILL"
IO_INTERRUPT="IO"
"""

"""im = new InterruptorManager
im.register(KILL_INTERRUPT, new KillHandler())
im.register(IO_INTERRUPT, new IOHandler())

cpu hace : 
   im.handle(irq)


Handler.handle(pcb)

self.irqDictionary["KILL_INTERRUPT"] = KillHandler()
"""