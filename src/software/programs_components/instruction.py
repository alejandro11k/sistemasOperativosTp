
class Instruction:
    
    def __init__(self,instructionType,instructionName):
        self.instructionType = instructionType
        self.name = instructionName
        
    def process(self):
        pass
    
    def isIO(self):
        return self.instructionType.name=="instructionIO"
        
        
    
    