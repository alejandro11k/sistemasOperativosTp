
class HardDisk:
    
    def __init__(self):
        self.programs = {}

    def find(self,programName):
        '''
        CUANDO UN PROGRAMCA NO SE ENCUENTRA DEBERIA TIRAR UNA EXCEPCION O SIMIL
        '''
        return self.programs[programName]
    
    def save(self,program):
        self.programs[program.name] = program