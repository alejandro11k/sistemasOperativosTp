class PageTable:
    
    #se encarga de traducir dirs virtuales en dirs físicas
    
    def __init__(self):
        self.pageTable = {}
    
    def put (self, adress):
        if self.isStored(adress):
            self.pageTable[adress] = 1 #flag que indica que sí está guardada en mem física
        else: 
            self.pageTable[adress] = 0 #flag que indica que no está guardada en mem física FALLO DE PÁG?
            self.pageFault(adress)
        
    def pageFault(self, adress):
        pass
        
    def isStored (self, adress):
        #if it's in real memory or not
        pass
    
    
        