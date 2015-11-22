from hardware.irq import Irq
from hardware.irq_type import IrqType

class Shell:
    
    def __init__ (self, interruptorManager):
        self.interruptorManager = interruptorManager
              
    def ps(self):
        #TODO
        #Mostrar todos los procesos y sus estados
        #self.programLoader.printPcbTable()
        pass
        
    def run(self, nameProgram):
        #self.programLoader.load(nameProgram)
        #lanzar interrupcion new
        #en ves de pasarle un pcb le paso el nombre del programa
        #CONSULTAR!!!
        self.irq = Irq(IrqType.irqNEW, nameProgram)
        self.interruptorManager.handle(self.irq)
        
        
    def ls(self):
        #Muestra los programas que se encuentran en el disco rigido
        pass
    
    