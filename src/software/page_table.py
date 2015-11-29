class PageTable:
    
    #se encarga de traducir dirs virtuales en dirs físicas
    
    def __init__(self):
        self.pageTable = {}
    
    def put (self, adress):
        if self.isStored(adress):
            self.pageTable[adress] = 1
        else: self.pageTable[adress] = 0   
        
        
    def isStored (self, adress):
        #if it's in real memory or not
        pass
    
        