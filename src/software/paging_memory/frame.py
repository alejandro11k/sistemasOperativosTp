
class Frame:
    
    def __init__(self,idFrame,size):
        self.page = None
        self.firstMemoryDirection = None
        self.size = size
        self.idFrame = idFrame
        self.calculateFirstMemoryDirection()
        self.longevity = None
        self.isFree = True
        
    def calculateFirstMemoryDirection(self):
        self.firstMemoryDirection = self.size * self.idFrame
    
    
