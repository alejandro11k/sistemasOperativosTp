class HandlerProcess:
     
    def __init__(self,scheduler):
        self.scheduler = scheduler
    
    #pseudocodigo
    
    #le dice al squedler que saque una instruccion de qReady 
    #realiza el setPCB al cpu, si este esta idle?
    
  
    def run(self):
        self.handle()
        
    def handle(self,pcb):
        print("process handler in action!")
        self.pcb = self.schedule.roundRobinQuantum(2)
        self.cpu.setPCB(self.pcb)
        