class PageTable:
    
    #se encarga de traducir dirs virtuales en dirs f�sicas
    
    def __init__(self):
        self.pageTable = {}
    
    def put (self, adress):
        if self.isStored(adress):
            self.pageTable[adress] = 1 #flag que indica que s� est� guardada en mem f�sica
        else: 
            self.pageTable[adress] = 0 #flag que indica que no est� guardada en mem f�sica FALLO DE P�G?
            self.pageFault(adress)
        
    def pageFault(self, adress):
        pass
        
    def isStored (self, adress):
        #if it's in real memory or not
        pass
    
    
        