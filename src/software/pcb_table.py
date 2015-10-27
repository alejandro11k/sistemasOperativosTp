class PCBTable:

    def __init__(self):
        self.pcbs = []
        
    def add (self, pcb):
        self.pcbs.append(pcb)
        
    def nextFreeId(self):
        return len(self.pcbs) + 1
        
        