from threading import Thread, RLock

class InterruptionManagerV2:
    
    #este im implementa una cola de irq
    
    def __init__(self,handler_data):
        self.handler_data = handler_data
        self.im_lock = RLock()
        self.handler = None
        
    def handle(self, irq):
        
        #buscar en el diccionario el handler correspondiente
        handler = self.handler_data.getHandler(irq.typeOfIrq)
        
        #aca se ejecuta el handle encontrado run
        self.register(irq,handler)
    
    def register(self,irq,handler):
        pass
        #add to a queue
        
    def runNextIrq(self):
        
        with self.im_lock:
            pass
            #if self.cpu.isIdle
            #take first irq
            
        #self.handler.run()
        
        
        

