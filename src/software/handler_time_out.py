from hardware.cpu import CPU
from software.q_ready import QReady

class HandlerTimeOut:

    def __init__ (self,cpu,qready):
        self.pcb = None
        self.cpu = cpu
        self.qready = qready

    def run(self,irq):
        self.handle(irq.pcb)
        
    def handle(self,pcb):
        self.pcb = pcb

    #pseudocodigo que hace 
    #libera el cpu
    #envia el pcb a la cola de ready
    
        print("time out handle in action!")

        if not (self.cpu.irq == None):
            self.cpu.pcb = None
            self.cpu.instruction = None
            self.cpu.irq = None
            
            self.qready.queue(pcb)