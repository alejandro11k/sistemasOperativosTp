import unittest

from software.handler_io import HandlerIO
from software.pcb import PCB
from software.process_states import ProcessStates
from software.q_io import QIo
from hardware.io_device import IoDevice
from software.instruction_type import InstructionType
from software.instruction import Instruction
from hardware.cpu import CPU

class Test(unittest.TestCase):

    def setUp(self):
    
        self.memory = None
        self.cpu = CPU(self.memory)
        self.handlerIO = HandlerIO(self.cpu, self.memory)
        
        self.instructionIO = InstructionType.instructionIO
        self.instructionPrint = Instruction(self.instructionIO,"PRINT")
        
        self.pcbRunning = PCB(1)
        self.pcbRunning.state = ProcessStates.processRunning
        self.dev1qio = QIo()
        self.dev2qio = QIo()
        self.ioDev1 = IoDevice("teclado",self.memory)
        self.ioDev2 = IoDevice("pantalla",self.memory)

    def tearDown(self):
        pass


    def test_when_add_device_queue_is_correctly_stored(self):
        self.handlerIO.addDevice(self.ioDev1,self.dev1qio)
        self.assertEquals(self.handlerIO.ioQueues[self.ioDev1],self.dev1qio)
    
    def test_when_handle_a_pcb_then_correctly_queued(self):
        self.handlerIO.addDevice(self.ioDev1, self.dev1qio)    
        self.handlerIO.addDevice(self.ioDev2, self.dev2qio)
        
        self.ioDev2.learnInstruction(self.instructionPrint)
        self.cpu.instruction = self.instructionPrint
        self.handlerIO.handle(self.pcbRunning)
              
        self.assertEquals(0, len(self.dev1qio.pcbs))
        self.assertEquals(1, len(self.dev2qio.pcbs))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()