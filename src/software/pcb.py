from software.process_states import ProcessStates 


class PCB:

    def __init__(self, idProcess):
        self.idProcess = idProcess
        self.programCounter = 0
        self.baseDirection = None
        self.state = ProcessStates.processReady
        self.lastDirection = None

    def incrementProgramCounter(self):
        self.programCounter = self.programCounter + 1
        
    def fillDirections(self, baseDirection, lastDirection):
        self.baseDirection = baseDirection
        self.lastDirection = lastDirection
        
    def setState(self, state):
        self.state = state
        