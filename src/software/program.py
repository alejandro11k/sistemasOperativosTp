from software.myQueue import MyQueue

class Program:
    
    def __init__(self,name):
        self.name = None
        self.instructionsList = MyQueue()
        
    def nextInstruction(self):
        return self.instructionsList.firstQ()
    
    def isLastInstuction(self):
        return (self.instructionsList.elements() == 1)