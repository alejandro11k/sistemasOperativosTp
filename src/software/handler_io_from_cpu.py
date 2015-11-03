from software.process_states import ProcessStates 

class HandlerIOfromCPU:

    def __init__ (self,cpu):
        
        self.pcb = None
        self.ioQueues = {}
        self.cpu = cpu
        
    def run(self,irq):
        self.handle(irq.pcb)
        
    def handle(self,pcb):
        self.pcb = pcb
 
        print("io handle (from cpu) in action!")
            
        self.cpu.pcb = None
        ioInstruction = self.cpu.instruction

        self.cpu.instruction = None
        self.cpu.irq = None
        self.cpu.quantum = 0
            
        self.pcb.state = ProcessStates.processWaiting
            
        ## envia a la cola d io
        ## la cola de io correspondiente a esa instruccion
            
        for k in self.ioQueues:
            if k.knownInstruction(ioInstruction):
                self.ioQueues[k].queue(pcb)
            
    def addDevice(self,ioDevice,ioQ):
        self.ioQueues[ioDevice]=ioQ
        