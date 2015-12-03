class PCBTable:

    def __init__(self):
        self.pcbs = []
        self.lastUsedId = 0
        
    def add (self, pcb):
        self.pcbs.append(pcb)
        
    def nextFreeId(self):
        self.lastUsedId = self.lastUsedId + 1
        return self.lastUsedId
    
    def printPcbTable(self):
        #podria ser un programa io?
        if len(self.pcbs)==0:
            print("empty pcb table")
        for n in self.pcbs:
            print ("id:",n.idProcess,"state:",n.state,"name:",n.program.name)
        
    def remove (self,pcb):
        index = self.pcbs.index(pcb)
        self.pcbs.pop(index) 