from hardware.irq import Irq
from hardware.irq_type import IrqType
from threading import Thread, RLock
from logging import threading
from time import sleep

class Shell:
    
    def __init__ (self, interruptorManager,pcbTable,hardDisk):
        Thread.__init__(self)
        self.interruptorManager = interruptorManager
        self.pcbTable = pcbTable
        self.hardDisk = hardDisk
              
    def ps(self):
        #TODO
        #Mostrar todos los procesos y sus estados
        print ("--------------------------------------------------------------")
        self.pcbTable.printPcbTable()
        print ("--------------------------------------------------------------")
        
    def load(self, nameProgram):
        #self.programLoader.load(nameProgram)
        #lanzar interrupcion new
        #en ves de pasarle un pcb le paso el nombre del programa
        #CONSULTAR!!!
        self.irq = Irq(IrqType.irqNEW, nameProgram)
        self.interruptorManager.handle(self.irq)
        
        
    def ls(self):
        #Muestra los programas que se encuentran en el disco rigido
        print ("---------------------------------------")
        print(self.hardDisk.ls())
        print ("---------------------------------------")
        
    def services(self,service):
        
        if service=="help":
            self.help()
            service = "OK"
        if service=="ls":
            self.ls()
            service = "OK"
        if service=="ps":
            self.ps()
            service = "OK"
        if not service=="OK":
            print ("---------------------------------------")
            print ("UNKNOW SERVICE OR PROGRAM -- type >help")
            print ("---------------------------------------")
    
    
    def help(self):
        print ("---------------------------------") 
        print ("COMMANDS:")
        print ("ls - show programs in hard disk")
        print ("ps - show pcb table")
        print ("---------------------------------")
    
    def start(self):
        result=input("PROGRAMA A EJECUTAR<:>")
        self.load(result)
            
    def run(self):
        Thread.run(self)
        self.start()
        