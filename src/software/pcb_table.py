class PCBTable:

    def __init__(self):
        self.pcbs = []
        
    def add (self, pcb):
        self.pcbs.append(pcb)
        
    def nextFreeId(self):
        return len(self.pcbs) + 1
    
    def printPcbTable(self):
        #podria ser un programa io?
        if len(self.pcbs)==0:
            print("empty pcb table")
        for n in self.pcbs:
            print ("id:",n.idProcess,"state:",n.state)
        
    def remove (self,pcb):
        index = self.pcbs.index(pcb)
        self.pcbs.pop(index) 