from software.processStates import ProcessStates 
from pickle import NONE


class PCB:

    def __init__(self, idProcess):
        self.idProcess = idProcess
        self.programCounter = 0
        self.baseDirection = None
        self.state = ProcessStates.processNew
        self.lastDirection = None

    def incrementPC(self):
        self.programCounter = self.programCounter + 1
        
    def fillDirections(self, baseDirection, lastDirection):
        self.baseDirection = baseDirection
        self.lastDirection = lastDirection
        
    def setState(self, state):
        self.state = state
        