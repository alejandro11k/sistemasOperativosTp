class LogicalMemory:
  
    def __init__(self, memory, pageTable):
        
        self.memory = memory
        self.pcb = None
        self.pageTable = pageTable
       
        