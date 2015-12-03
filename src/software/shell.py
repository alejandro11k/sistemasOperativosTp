from hardware.irq import Irq
from hardware.irq_type import IrqType
from threading import Thread, RLock
from logging import threading
from time import sleep

class Shell:
    
    def __init__ (self, interruptorManager):
        Thread.__init__(self)
        self.interruptorManager = interruptorManager
              
    def ps(self):
        #TODO
        #Mostrar todos los procesos y sus estados
        #self.programLoader.printPcbTable()
        pass
        
    def load(self, nameProgram):
        #self.programLoader.load(nameProgram)
        #lanzar interrupcion new
        #en ves de pasarle un pcb le paso el nombre del programa
        #CONSULTAR!!!
        self.irq = Irq(IrqType.irqNEW, nameProgram)
        self.interruptorManager.handle(self.irq)
        
        
    def ls(self):
        #Muestra los programas que se encuentran en el disco rigido
        pass
    
    def start(self):
        result=input("PROGRAMA A EJECUTAR<:>")
        self.load(result)
            
    def run(self):
        Thread.run(self)
        self.start()
        