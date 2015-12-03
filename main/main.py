from hardware.memory import Memory, LimitedMemory
from hardware.cpu import CPU
from hardware.hard_disk import HardDisk
from software.interruption_manager import InterruptionManager
from software.pcb import PCB
from software.programs_components.program import Program
from software.shell import Shell
from software.pcb_table import PCBTable
from software.q_ready import QReady
from software.scheduler import Schedule
from software.q_io import QIo
from hardware.io_device import IoDevice
from software.handlers.handlers import Handlers
from hardware.clock import Clock
from time import sleep
from software.programs_components.programs import Programs
from software.paging_memory.logical_memory import LogicalMemory

if __name__ == '__main__':

        #hardware
        #construyo el ordenador
        hardDisk = HardDisk()
        #self.memory = Memory()
        memorySize = 12
        memory = LimitedMemory(memorySize)
        cpu = CPU(memory)
        ioDevice = IoDevice("IOdevice OUT")
        ioDevice2 = IoDevice("IOdevice IN")

        #kernel
        qReady = QReady()
        qIo = QIo()
        qIo2 = QIo()
        pcbTable = PCBTable()
        scheduler = Schedule(qReady,cpu,2)
        
        #test new memory model, need change irqNew to irqNew2 in handler class
        realMemory = memory
        pageSize = 4 # FRAME SIZE
        memory = LogicalMemory(memory,pageSize)
        
        interruptionManager = InterruptionManager(cpu,scheduler)
        cpu.setUp(interruptionManager,memory)
        
        ioDevice.setUp(interruptionManager,qIo,memory)
        ioDevice2.setUp(interruptionManager,qIo2,memory)
        
        shell = Shell(interruptionManager,pcbTable,hardDisk)
        
        handlers = Handlers(interruptionManager,cpu,
                                 pcbTable,scheduler,qReady,
                                 hardDisk,memory,shell)
        
        #el handler conoce el device
        handlers.handlerIOfromCPU.addDevice(ioDevice, qIo)
        handlers.handlerIOfromCPU.addDevice(ioDevice2, qIo2)
        
        #agrego programas al disco
        programs = Programs()
        
        for n in range(len(programs.programs)):
            hardDisk.save(programs.programs.pop(0))
        
        #el device conoce la instruccion
        
        ioDevice.learnInstruction(programs.instructions['PRINT'])
        ioDevice2.learnInstruction(programs.instructions['INPUT'])
        ioDevice2.learnInstruction(programs.instructions['realINPUT'])
        
        ciclos = 2000 #batery
        clock = Clock(interruptionManager,cpu,ioDevice,ioDevice2,ciclos)
        
        shell.load("realINPUT")
        clock.run()
       

