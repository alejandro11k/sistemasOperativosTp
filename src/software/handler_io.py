class HandlerIO:

    def __init__ (self):
        self.pcb = None

    def run(self,irq):
        self.handle(irq.pcb)
        
    def handle(self,pcb):
        self.pcb = pcb

    ## pseudocodigo que hace.
        print("io handle in action!")
