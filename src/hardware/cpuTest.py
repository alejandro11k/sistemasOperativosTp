import unittest

from hardware.memory import Memory
from hardware.cpu import CPU
from software.interruptionManager import InterruptionManager
from software.pcb import PCB

class TestCPU(unittest.TestCase):


    def setUp(self):
        self.pcb = PCB(0,2)

        self.memory = Memory()
        self.memory.put(0,"primer instruccion")
        self.memory.put(1,"segunda instruccion")

        self.im = InterruptionManager()

        self.cpu = CPU(self.memory,self.im)
        
    def test_fecht(self):
        self.assertTrue(True)

    #ejecuto un programa que termina
    def test_incrementPC(self):
        self.cpu.setPCB(self.pcb)
        self.assertEquals(self.cpu.programCounter,0)



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