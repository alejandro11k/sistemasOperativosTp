
class Frame:
    
    def __init__(self,idFrame,size):
        self.page = None
        self.firstMemoryDirection = None
        self.size = size
        self.idFrame = idFrame
        self.calculateFirstMemoryDirection()
        self.isFree = True
        self.timeAcces = 0
        
        
    def calculateFirstMemoryDirection(self):
        self.firstMemoryDirection = self.size * self.idFrame
    
    def bckpInstrutionsFromMemory(self,memory):
        bckp = []
        for n in range(self.size):
            instruction = memory.get(self.firstMemoryDirection+n)
            bckp.append(instruction)
        return bckp

    def reUse(self):
        self.page = None
        self.isFree = True
        
    def setPage(self,pageId):
        self.isFree = False
        self.page = pageId