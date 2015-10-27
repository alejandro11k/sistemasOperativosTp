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


class CpuTest(unittest.TestCase):

    '''
    este test esta desactualizado, y las clases nuevas estan
    en proceso
    '''

    def setUp(self):

        self.im = InterruptionManager()

        #hardware
        #construyo el ordenador
        self.hardDisk = HardDisk()
        self.memory = Memory()
        self.cpu = CPU(self.memory,self.im)

        #kernel
        self.pcbTable = PCBTable()
        self.qReady = QReady()
        self.programLoader = ProgramLoader(self.hardDisk,self.memory,self.pcbTable,self.qReady)
        self.shell = Shell(self.programLoader)
        self.schedule = Schedule(self.qReady,self.cpu)
        
        #crep un programa
        self.instruction0 = Instruction(InstructionType.instructionEND)
        self.instruction1 = Instruction(InstructionType.instructionCPU)
        instructions = []
        instructions.append(self.instruction1)
        instructions.append(self.instruction0) #revisar orden!
        
        self.program = Program("empty_program")
        self.program.compileInstructions(instructions)
        
        #guardo el programa en el disco rigido
        self.hardDisk.save(self.program)
     
        
    def test_ejecutoUnProgramaConUnaUnicaInstruccionDeEnd(self):
        self.shell.run("empty_program")
        self.schedule.roundRobinQuantum(10)
        self.cpu.fetch()
        self.cpu.fetch()
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