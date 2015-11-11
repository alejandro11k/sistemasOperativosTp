class InterruptionManager:
    
    def __init__(self,handler_data):
        self.handler_data = handler_data
        self.pendingToProcessIrqs = [] 
        
    def handle(self, irq):
        self.pendingToProcessIrqs.append(irq)
    
    def fetch(self):
        for irq in self.pendingToProcessIrqs :
            self.run(irq)
            
        self.pendingToProcessIrqs.clear()
    
    def run(self, irq):
        #buscar en el diccionario el handler correspondiente
        handler = self.handler_data.getHandler(irq.typeOfIrq)
        
        #aca se ejecuta el handle encontrado run

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