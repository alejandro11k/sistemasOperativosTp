from software.process_states import ProcessStates 

class HandlerIOfromIO:

    def __init__ (self,qready):
        
        self.pcb = None
        self.qready = qready
        
    def run(self,irq):
        self.handle(irq.pcb)
        
    def handle(self,pcb):
        self.pcb = pcb

        print("io handle (from io) in action!")
        self.pcb.state = ProcessStates.processReady
        self.qready.queue(pcb)