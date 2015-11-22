
class HardDisk:
    
    def __init__(self):
        self.programs = {}

    def find(self,programName):
        return self.programs[programName]
    
    def save(self,program):
        self.programs[program.name] = program