from software.program_loader import ProgramLoader

class Shell:
    
    def __init__ (self, programLoader):
        self.programLoader = programLoader
              
    def ps(self):
        pass
        #TODO
        #Mostrar todos los procesos y sus estados.
        
    def run(self, nameProgram):
        self.programLoader.load(nameProgram)
    
    