from software.processStates import ProcessStates 


class PCB:

    def __init__(self, baseDirection,lastDirection):
        self.idProcess = 0
        self.programCounter = 0
        self.baseDirection = baseDirection
        self.state = ProcessStates.processNew
        self.lastDirection = lastDirection

    def incrementPC(self):
            
        self.programCounter = self.programCounter + 1
        