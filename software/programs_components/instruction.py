
class Instruction:
    
    def __init__(self,instructionType,instructionName):
        self.instructionType = instructionType
        self.name = instructionName
        
    def process(self):
        result = None
        if self.name=="realINPUT":
            result =  input("PROGRAMA A EJECUTAR<:>")
        return result
    
    def isIO(self):
        return self.instructionType.name=="instructionIO"
        
        
    
    