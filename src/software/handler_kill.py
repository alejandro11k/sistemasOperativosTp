class HandlerKill:

    def __init__ (self,cpu,pcbtable):
        self.pcb = None
        self.cpu = cpu
        self.pcbtable = pcbtable

    def run(self,irq):
        self.handle(irq.pcb)
        
    def handle(self,pcb):
        self.pcb = pcb

    ## pseudocodigo que hace.
    ## libera el cpu
    ## limpia la memoria correspondiente a ese pcb TODO
    ## mata el proceso TODO
    
        print("kill handle in action!")
        
        if not (self.cpu.irq == None):
            self.cpu.pcb = None
            self.cpu.instruction = None
            self.cpu.irq = None
            self.cpu.quantum = 0
            
            self.pcbtable.remove(self.pcb)
