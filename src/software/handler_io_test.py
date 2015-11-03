import unittest

from software.handler_io import HandlerIO
from software.pcb import PCB
from software.process_states import ProcessStates
from software.q_io import QIo
from hardware.io_device import IoDevice

class Test(unittest.TestCase):

    def setUp(self):
        
        self.cpu = None
        self.memory = None
        self.handlerIO = HandlerIO(self.cpu, self.memory)
        
        self.pcbRunning = PCB(1)
        self.pcbRunning.state = ProcessStates.processRunning
        self.dev1qio = QIo()
        self.dev2qio = QIo()
        self.ioDev1 = IoDevice("pantalla",self.memory)
        self.ioDev2 = IoDevice("teclado",self.memory)

    def tearDown(self):
        pass


    def test_when_add_device_queue_is_correctly_stored(self):
        self.handlerIO.addDevice(self.ioDev1,self.dev1qio)
        self.assertEquals(self.handlerIO.ioQueues[self.ioDev1],self.dev1qio)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()