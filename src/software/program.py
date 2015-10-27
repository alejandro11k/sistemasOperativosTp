from software.my_queue import MyQueue

class Program:
    
    '''
    Un programa debe contener al menos una instruccion de fin    
    '''
    
    def __init__(self,name):
        self.name = name
        self.instructionsList = MyQueue()
        
    def nextInstruction(self):
        return self.instructionsList.firstQ()
    
    def isLastInstuction(self):
        cantidadDeInstruccionesPorEjecutar = self.instructionsList.size()
        return (cantidadDeInstruccionesPorEjecutar==1)
        