from software.program_loader import ProgramLoader

class Shell:
    
    def __init__ (self, programLoader):
        self.programLoader = programLoader
              
    def ps(self):
        #TODO
        #Mostrar todos los procesos y sus estados
        self.programLoader.printPcbTable()
        
        
    def run(self, nameProgram):
        self.programLoader.load(nameProgram)
        
    def ls(self):
        #Muestra los programas que se encuentran en el disco rigido
        pass
    
    