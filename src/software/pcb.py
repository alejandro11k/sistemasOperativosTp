from software.processStates import ProcessStates 


class PCB:

    def __init__(self, baseDirection,instructions):
        self.idProcess = 0
        self.programCounter = 0
        self.baseDirection = baseDirection
        self.state = ProcessStates.processNew
        # cantidad total de instrucciones
        self.instructions = instructions

    def incrementPC(self):
            
        self.programCounter = self.programCounter + 1
        