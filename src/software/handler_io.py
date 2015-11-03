from software.process_states import ProcessStates 

class HandlerIO:

    def __init__ (self,cpu,qready):
        
        self.pcb = None
        self.ioQueues = {}
        self.cpu = cpu
        #only one io devise at the moment
        self.ioQueue = None
        self.qready = qready
        
    def run(self,irq):
        self.handle(irq.pcb)
        
    def handle(self,pcb):
        self.pcb = pcb

    ## pseudocodigo que hace.
    ## limpia la cpu
    ## envia el pcb a la cola de io
    
        result = self.pcb.programCounter-1 + self.pcb.baseDirection
        instruction = self.memory.get(result) 
        
        #if pcb.state==ProcessStates.processRunningIO:
        if instruction.isIO():
            print("io handle (from io) in action!")
            
            self.pcb.state = ProcessStates.processReady
            
            self.qready.queue(pcb)
        
        if pcb.state==ProcessStates.processRunning: #and not (self.cpu.irq == None):
            
            print("io handle (from cpu) in action!")
            
            self.cpu.pcb = None
            ioInstruction = self.cpu.instruction

            self.cpu.instruction = None
            self.cpu.irq = None
            self.cpu.quantum = 0
            
            self.pcb.state = ProcessStates.processWaiting
            ## envia a la cola d io
            ## la cola de io correspondiente a esa instruccion
            ## por ahora solo hay una unica io
            
            for k in self.ioQueues:
                if k.knownInstruction(ioInstruction):
                    self.ioQueues[k].queue(pcb)
                    
            #self.ioQueues[ioDev].queue(pcb)
            #self.ioQueue.queue(pcb)
            
    def addDevice(self,ioDevice,ioQ):
        self.ioQueues[ioDevice]=ioQ
        #self.ioQueue=ioQ
