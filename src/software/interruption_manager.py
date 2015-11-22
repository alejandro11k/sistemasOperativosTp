from hardware.cpu import CPU
class InterruptionManager:
    
    def __init__(self,cpu,scheduler):
        self.cpu = cpu
        self.scheduler = scheduler
        self.pendingToProcessIrqs = []
        #Handler container and IRQ correspondence
        self.irqRoutines = {} 
    
    def handle(self, irq):
        self.pendingToProcessIrqs.append(irq)
        
        
    def switch(self):
        if self.cpu.isIdle():
            self.scheduler.giveOne()
    
    def fetch(self):
        for irq in self.pendingToProcessIrqs :
            self.run(irq)
            self.switch()
            
        self.pendingToProcessIrqs.clear()
    
    def run(self, irq):
        #buscar en el diccionario el handler correspondiente
        handler = self.getHandler(irq.typeOfIrq)
        #aca se ejecuta el handle encontrado run
        handler.run(irq)
    
    def register(self,irqType,handler):
        self.irqRoutines[irqType.name] = handler
        
    def getHandler(self,irqType):
        handler = self.irqRoutines[irqType.name]
        return handler   

