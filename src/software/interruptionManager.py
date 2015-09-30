from software.killHandler import KillHandler

class InterruptionManager:
    
    def __init__(self):
        self.irqDictionary = {}
        self.initializeDictionary()
        self.handler = None
        
    def initializeDictionary(self):
        self.irqDictionary["KILL_INTERRUPT"] = KillHandler()
        #setear desde afuera, estos es un registrer

    def handle(self, irq):
        
        
        #buscar en el diccionario el handler correspondiente
        self.handler = self.irqDictionary[irq.typeOfIrq]
        
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
"""