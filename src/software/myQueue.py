class MyQueue:
    
    
    def __init__(self):
        self.list = []
        self.elements = 0
        
    def firstQ(self):
        #si no tengo elementos rompe
        self.list.pop(0)
        
    def queue(self,element):
        self.append(element)
        self.elements = self.elements + 1
        
    def isEmpty(self):
        return (self.elements == 0)
        