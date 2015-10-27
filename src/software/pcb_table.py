class PCBTable:

    def __init__(self):
        '''
        Constructor
        '''
        self.pcbs = []
        
        
    def add (self, pcb):
        self.pcbs.append(pcb)
        
    def nextFreeId(self):
        return self.pcbs.length + 1
        
        