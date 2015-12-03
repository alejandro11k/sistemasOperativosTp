from software.my_queue import MyQueue

class QIo():

    def __init__(self):
        self.pcbs = []
        self.pcbsN = 0
        
    def queue(self,pcb):
        self.pcbs.append(pcb)
        self.pcbsN+=1
        
    def getFirst(self):
        #empty pcbs broke
        pcb = self.pcbs.pop(0)
        self.pcbsN-=1
        return pcb
    
    def emptyQ(self):
        value = self.pcbsN==0
        return value