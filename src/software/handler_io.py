class HandlerIO:

    def __init__ (self):
        self.pcb = None
        self.ioQs = {}

    def run(self,irq):
        self.handle(irq.pcb)
        
    def handle(self,pcb):
        self.pcb = pcb

    ## pseudocodigo que hace.
    ## limpia la cpu
    ## envia el pcb a la cola de io
    
        print("io handle in action!")
        
        if not (self.cpu.irq == None):
            self.cpu.pcb = None
            ioDev = self.cpu.instruction = None
            self.cpu.irq = None
            
            ## envia a la cola d io
            ## la cola de io correspondiente a esa instruccion
            ## por ahora solo hay una unica io
            
            self.qIO[ioDev.instructionType.value].queue(pcb)
            
    def addDevice(self,instructionType,qIO):
        self.ioQs[instructionType.value]=qIO
        
