from software.process_states import ProcessStates 

class HandlerIO:

    def __init__ (self,cpu):
        self.pcb = None
        self.ioQueues = {}
        self.cpu = cpu
        #only one io devise at the moment
        self.ioQueue = None

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
            ioDev = self.cpu.instruction
            self.cpu.instruction = None
            self.cpu.irq = None
            self.cpu.quantum = 0
            
            self.pcb.state = ProcessStates.processWaiting
            ## envia a la cola d io
            ## la cola de io correspondiente a esa instruccion
            ## por ahora solo hay una unica io
            
            #self.ioQueues[ioDev.instructionType.name].queue(pcb)
            self.ioQueue.queue(pcb)
            
    def addDevice(self,instructionType,ioQ):
        #self.ioQueues[instructionType.name]=ioQ
        self.ioQueue=ioQ
