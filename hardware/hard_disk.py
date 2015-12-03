
class HardDisk:
    
    def __init__(self):
        self.programs = {}

    def find(self,programName):
        if programName in self.programs:
            return self.programs[programName]
        else:
            return None
    
    def save(self,program):
        self.programs[program.name] = program
        
    def ls(self):
        return list(self.programs.keys())