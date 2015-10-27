from software.my_queue import MyQueue

class Program:
    
    '''
    Un programa debe contener al menos una instruccion de fin    
    '''
    
    def __init__(self,name):
        self.name = None
        self.instructionsList = MyQueue()
        
    def nextInstruction(self):
        return self.instructionsList.firstQ()
    
    def isLastInstuction(self):
        return (self.instructionsList.elements() == 1)
        