class Instruction:
    
    def __init__(self,instructionType,instructionName):
        self.instructionType = instructionType
        self.name = instructionName
        
    def process(self,foo):
        pass
    
    def isIO(self):
        return self.instructionType.name=="instructionIO"
        
class RealInstruction(Instruction):
    
    def __init__(self,instructionType,instructionName):
        super().__init__(instructionType,instructionName)
        self.nameProgram = None
        
    def process(self,interruptionManager):
        if self.name=="realINPUT":
            self.nameProgram=input("accion:")
            interruptionManager.runProgram(self.nameProgram) 
    
    def isIO(self):
        return self.instructionType.name=="instructionIO"        
    
    