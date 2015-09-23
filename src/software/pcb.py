class PCB:

    def __init__(self, baseDirection,instructions):
        self.programCounter = 0
        self.baseDirection = baseDirection

        # cantidad total de instrucciones
        self.instructions = instructions

    def incrementPC(self):
            
        self.programCounter = self.programCounter + 1
        