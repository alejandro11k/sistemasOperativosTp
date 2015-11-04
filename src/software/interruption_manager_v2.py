class InterruptionManagerV2:
    
    def __init__(self,handler_data):
        self.handler_data = handler_data
        
    def handle(self, irq):
        
        #buscar en el diccionario el handler correspondiente
        handler = self.handler_data.getHandler(irq.typeOfIrq)
        
        #aca se ejecuta el handle encontrado run
        self.register(irq,handler)
    
    def register(self,irq,handler):
        pass
        #add to a queue
        
    def runNextIrq(self):
        pass
        #if self.cpu.isIdle
        
        #else
        
        #self.handler.run()

