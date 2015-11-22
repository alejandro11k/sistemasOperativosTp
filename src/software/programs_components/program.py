from dis import Instruction
class Program:
    
    '''
    Un programa debe contener al menos una instruccion de fin    
    '''
    
    def __init__(self,name):
        self.name = name
        self.instructionsList = {}
        
    def getInstruction(self,n):
        return self.instructionsList[n]
    
    def programLength(self):
        return len(self.instructionsList)
    
    def compileInstructions(self,instructions):
        #la ultima instruccion debe ser la de END!
        size = len(instructions)
        for n in range(size):
            self.instructionsList[n]=(instructions.pop(0))
            
        