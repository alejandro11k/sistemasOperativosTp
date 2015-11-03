import unittest

from memory import Memory
from cpu import CPU
from hardware.hard_disk import HardDisk

from software.interruption_manager import InterruptionManager
from software.pcb import PCB
from software.instruction import Instruction
from software.instruction_type import InstructionType
from software.program import Program
from software.shell import Shell
from software.program_loader import ProgramLoader
from software.pcb_table import PCBTable
from software.q_ready import QReady
from software.schedule import Schedule
from software.handler_data import HandlerData
from software.handler_kill import HandlerKill
from software.handler_time_out import HandlerTimeOut
from software.handler_io import HandlerIO
from hardware.irq_type import IrqType
from software.q_io import QIo
from hardware.io_device import IoDevice
from software.handler_io_from_cpu import HandlerIOfromCPU
from software.handler_io_from_io import HandlerIOfromIO


class CpuTest(unittest.TestCase):

    '''
    este test esta desactualizado, y las clases nuevas estan
    en proceso
    '''

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
        
        self.irqTypeKill = IrqType.irqKILL
        self.handlerKill = HandlerKill(self.cpu,self.pcbTable)
        
        self.irqTypeTimeOut = IrqType.irqTIME_OUT
        self.handlerTimeOut = HandlerTimeOut(self.cpu,self.qReady)
        
        #self.irqTypeIO = IrqType.irqIO
        #self.handlerIO = HandlerIO(self.cpu,self.qReady)
        
        self.irqTypeIOfromCPU = IrqType.irqIOfromCPU
        self.handlerIOfromCPU = HandlerIOfromCPU(self.cpu)
        
        self.irqTypeIOfromIO = IrqType.irqIOfromIO
        self.handlerIOfromIO = HandlerIOfromIO(self.qReady)
        
        
        self.handler_data = HandlerData()
        self.handler_data.setUp(self.irqTypeKill, self.handlerKill)
        self.handler_data.setUp(self.irqTypeTimeOut, self.handlerTimeOut)
        self.handler_data.setUp(self.irqTypeIOfromCPU, self.handlerIOfromCPU)
        self.handler_data.setUp(self.irqTypeIOfromIO, self.handlerIOfromIO)
        
        self.interruptionManager = InterruptionManager(self.handler_data)
        
        self.cpu.setUp(self.interruptionManager)
        self.ioDevice.setUp(self.interruptionManager,self.qIo)
        self.ioDevice.learnInstruction("PRINT")
        
        
        self.programLoader = ProgramLoader(self.hardDisk,self.memory,self.pcbTable,self.qReady)
        self.shell = Shell(self.programLoader)
        self.schedule = Schedule(self.qReady,self.cpu)
        
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
        
    def pruebaDeEjecucion1(self):
        
        self.shell.run("empty_program")
        self.schedule.roundRobinQuantum(2)
        self.cpu.fetch()
        self.cpu.fetch()
        self.cpu.fetch()
        self.cpu.fetch()
        self.schedule.roundRobinQuantum(2)
        self.cpu.fetch()
        self.cpu.fetch()
        self.cpu.fetch()
        
        self.assertTrue(True)
        
    def pruebaDeEjecucion2(self):
        
        self.shell.ps()
        
        self.shell.run("empty_program")
        self.shell.run("empty_program")
        self.shell.run("empty_program")
        
        self.shell.ps()
                      
        self.cpu.fetch()
        self.schedule.roundRobinQuantum(2)
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.cpu.fetch()
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.schedule.roundRobinQuantum(2)
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.cpu.fetch()
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.schedule.roundRobinQuantum(2)
        self.cpu.fetch()
        self.cpu.fetch()
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.schedule.roundRobinQuantum(2)
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.cpu.fetch()
        self.cpu.fetch()
        
        self.schedule.roundRobinQuantum(2)
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.cpu.fetch()
        self.cpu.fetch()
        
        self.shell.ps()
        
        self.schedule.roundRobinQuantum(2)
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
        self.schedule.roundRobinQuantum(2)
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
        
        self.schedule.roundRobinQuantum(2)
        self.cpu.fetch()
        self.shell.ps()
        self.cpu.fetch()
        self.shell.ps()
        
        self.assertTrue(True)

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