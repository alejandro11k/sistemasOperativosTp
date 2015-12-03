
class Frame:
    
    def __init__(self,idFrame,size):
        self.page = None
        self.firstMemoryDirection = None
        self.size = size
        self.idFrame = idFrame
        self.calculateFirstMemoryDirection()
        self.isFree = True
        self.timeAcces = 0
        self.instructionsQuantity = 0
        
        
    def calculateFirstMemoryDirection(self):
        self.firstMemoryDirection = self.size * self.idFrame
    
    def bckpInstrutionsFromMemory(self,memory):
        bckp = []
        for n in range(self.instructionsQuantity):
            instruction = memory.get(self.firstMemoryDirection+n)
            bckp.append(instruction)
        return bckp
    
    def restoreInstructionsToMemory(self,instructions,memory):
        for n in range(len(instructions)):
            address = self.firstMemoryDirection+n
            instruction = instructions.pop(0)
            memory.put(address,instruction)

    def reUse(self):
        self.page = None
        self.isFree = True
        
    def setPage(self,pageId,n):
        self.isFree = False
        self.page = pageId
        self.instructionsQuantity = n