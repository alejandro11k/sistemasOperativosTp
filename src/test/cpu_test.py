import unittest

from hardware.memory import Memory
from hardware.cpu import CPU
from hardware.hard_disk import HardDisk

from software.interruption_manager import InterruptionManager
from software.pcb import PCB
from software.programs_components.instruction import Instruction
from software.programs_components.instruction_type import InstructionType
from software.programs_components.program import Program
from software.shell import Shell
from software.pcb_table import PCBTable
from software.q_ready import QReady
from software.scheduler import Schedule
from software.handlers.handler_kill import HandlerKill
from software.handlers.handler_time_out import HandlerTimeOut
from hardware.irq_type import IrqType
from software.q_io import QIo
from hardware.io_device import IoDevice
from software.handlers.handler_io_from_cpu import HandlerIOfromCPU
from software.handlers.handler_io_from_io import HandlerIOfromIO
from software.handlers.handler_new import HandlerNew
from hardware.clock import Clock
from time import sleep



class CpuTest(unittest.TestCase):

    def setUp(self):
  

        #hardware
        #construyo el ordenador
        self.hardDisk = HardDisk()
        self.memory = Memory()
        self.cpu = CPU(self.memory)
        self.ioDevice = IoDevice("IOdevice",self.memory)

        #kernel
        self.qReady = QReady()
        self.qIo = QIo()
        self.pcbTable = PCBTable()
        
        self.scheduler = Schedule(self.qReady,self.cpu)
        
        
        self.interruptionManager = InterruptionManager(self.cpu,self.scheduler)
        self.irqTypeKill = IrqType.irqKILL
        self.handlerKill = HandlerKill(self.cpu,self.pcbTable,self.scheduler)
        
        self.irqTypeTimeOut = IrqType.irqTIME_OUT
        self.handlerTimeOut = HandlerTimeOut(self.cpu,self.qReady,self.scheduler)
        
        self.irqTypeIOfromCPU = IrqType.irqIOfromCPU
        self.handlerIOfromCPU = HandlerIOfromCPU(self.cpu)
        
        self.irqTypeIOfromIO = IrqType.irqIOfromIO
        self.handlerIOfromIO = HandlerIOfromIO(self.qReady)
        
        self.irqTypeNew = IrqType.irqNEW
        self.handlerNew = HandlerNew(self.hardDisk, self.memory, self.pcbTable, self.qReady, self.scheduler,self.cpu)

        self.interruptionManager.register(self.irqTypeKill, self.handlerKill)
        self.interruptionManager.register(self.irqTypeTimeOut, self.handlerTimeOut)
        self.interruptionManager.register(self.irqTypeIOfromCPU, self.handlerIOfromCPU)
        self.interruptionManager.register(self.irqTypeIOfromIO, self.handlerIOfromIO)
        self.interruptionManager.register(self.irqTypeNew, self.handlerNew)
        
        self.cpu.setUp(self.interruptionManager)
        self.ioDevice.setUp(self.interruptionManager,self.qIo)
        self.ioDevice.learnInstruction("PRINT")
        
        self.shell = Shell(self.interruptionManager)
        
        
        #crep un programa
        self.instructionEnd = Instruction(InstructionType.instructionEND,"KILL")
        self.instructionCpu = Instruction(InstructionType.instructionCPU,"SUM")
        instructions = []
        instructions.append(self.instructionCpu)
        instructions.append(self.instructionCpu)
        instructions.append(self.instructionCpu)
        instructions.append(self.instructionEnd)
        
        self.program = Program("empty_program")
        self.program.compileInstructions(instructions)
        
        #guardo el programa en el disco rigido
        self.hardDisk.save(self.program)
        
        #creo otro programa
        instructions = []
        self.instructionTypeIO = InstructionType.instructionIO
        self.instructionPrint = Instruction(self.instructionTypeIO,"PRINT")
        
        #self.instructionIO = Instruction(InstructionType.instructionIO,"PRINT")
        instructions.append(self.instructionCpu)
        instructions.append(self.instructionPrint)
        instructions.append(self.instructionEnd)
        
        self.programIO = Program("io_program")
        self.programIO.compileInstructions(instructions)
        
        self.hardDisk.save(self.programIO)
        
        #el handler conoce el device
        self.handlerIOfromCPU.addDevice(self.ioDevice, self.qIo)
        #el device conoce la instruccion print
        self.ioDevice.learnInstruction(self.instructionPrint)
        
        self.clock = Clock(self.interruptionManager,self.cpu,self.ioDevice)
        
        
    def pruebaDeEjecucionCpuPrograms(self):
        
        self.shell.run("empty_program")
        self.shell.run("empty_program")
        self.shell.run("empty_program")
        self.shell.run("empty_program")
        self.clock.run()
        
        self.assertTrue(True)
        
    def pruebaDeEjecucionCpuAndIoPrograms(self):
        
        self.shell.run("empty_program")
        self.shell.run("io_program")
        
        self.clock.run()
        
        self.assertTrue(True)
        
    '''
    def pruebaDeEjecucion2(self):
        
        self.shell.ps()
        
        self.shell.run("empty_program")
        self.shell.run("empty_program")
        self.shell.run("empty_program")
        
        self.shell.ps()
                      
        self.cpu.fetch()
        self.scheduler.roundRobinQuantum(2)
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.cpu.fetch()
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.scheduler.roundRobinQuantum(2)
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.cpu.fetch()
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.scheduler.roundRobinQuantum(2)
        self.cpu.fetch()
        self.cpu.fetch()
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.scheduler.roundRobinQuantum(2)
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.cpu.fetch()
        self.cpu.fetch()
        
        self.scheduler.roundRobinQuantum(2)
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.cpu.fetch()
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.scheduler.roundRobinQuantum(2)
        self.cpu.fetch()
        self.shell.run("empty_program")
        self.cpu.fetch()
        self.cpu.fetch()
        
        self.shell.run("empty_program")
        self.shell.ps()
            
        self.assertTrue(True)
        
    def pruebaDeEjecucion3(self):
        #programa con instruccion de io
        self.shell.run("io_program")
        self.scheduler.roundRobinQuantum(2)
        self.cpu.fetch()
        self.shell.ps()
        self.cpu.fetch()
        self.shell.ps()
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.ioDevice.setPCB()
        self.ioDevice.fetch()
        
        self.shell.ps()
        self.cpu.fetch()
        self.shell.ps()
        self.cpu.fetch()
        
        self.scheduler.roundRobinQuantum(2)
        self.cpu.fetch()
        self.shell.ps()
        self.cpu.fetch()
        self.shell.ps()
        
        self.assertTrue(True)
    '''

#unittest.main(verbosity=2)

'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
'''