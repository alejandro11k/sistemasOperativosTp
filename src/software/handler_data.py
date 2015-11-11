class HandlerData:
    #BORRRARRRR
    '''
    Handler container and IRQ correspondence
    '''
    def __init__(self):
        self.irqDictionary = {}
    
    def setUp(self,irqType,handler):        
        self.irqDictionary[irqType.name] = handler
        
    def getHandler(self,irqType):
        handler = self.irqDictionary[irqType.name]
        return handler
    
    def addHandler(self, iRQtype,irqHandler):
        self.irqDictionary[iRQtype] = irqHandler
