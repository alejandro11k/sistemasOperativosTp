class InterruptionManager:
    
    def __init__(self,handler_data):
        self.handler_data = handler_data
        
    def handle(self, irq):
        
        #buscar en el diccionario el handler correspondiente
        handler = self.handler_data.getHandler(irq.typeOfIrq)
        
        #aca se ejecuta el handle encontrado run
        self.register(irq,handler)
    
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