class Clock:
    
    def __init__(self,device):
        self.device = device
        
    def click(self):
        self.device.fetch()