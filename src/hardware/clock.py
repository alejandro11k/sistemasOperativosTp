from hardware.cpu import CPU

class Clock:
    
    def __init__(self,cpu):
        self.cpu = cpu
        
    def click(self):
        self.cpu.fetch()