import unittest
from hardware.irq_type import IrqType
from software.handler_new import HandlerNew
from software.handler_process import HandlerProcess
from software.handler_io_from_cpu import HandlerIOfromCPU
from software.handler_io_from_io import HandlerIOfromIO
from software.handler_kill import HandlerKill
from software.handler_time_out import HandlerTimeOut
from software.handler_data import HandlerData
from software.interruption_manager_v2 import InterruptionManagerV2

class Test(unittest.TestCase):


    def setUp(self):
        self.irqTypeKill = IrqType.irqKILL
        self.handlerKill = HandlerKill("self.cpu","self.pcbTable")
        
        self.irqTypeTimeOut = IrqType.irqTIME_OUT
        self.handlerTimeOut = HandlerTimeOut("self.cpu","self.qReady")
        
        self.irqTypeIOfromCPU = IrqType.irqIOfromCPU
        self.handlerIOfromCPU = HandlerIOfromCPU("self.cpu")
        
        self.irqTypeIOfromIO = IrqType.irqIOfromIO
        self.handlerIOfromIO = HandlerIOfromIO("self.qReady")
        
        self.irqTypeNew = IrqType.irqNEW
        self.handlerNew = HandlerNew("pcbTable","hardDisk","memory","qReady")
        
        self.irqTypeProcess = IrqType.irqProcess
        self.handlerProcess = HandlerProcess()
        
        self.handler_data = HandlerData()
        self.handler_data.setUp(self.irqTypeKill, self.handlerKill)
        self.handler_data.setUp(self.irqTypeTimeOut, self.handlerTimeOut)
        self.handler_data.setUp(self.irqTypeIOfromCPU, self.handlerIOfromCPU)
        self.handler_data.setUp(self.irqTypeIOfromIO, self.handlerIOfromIO)
        
        self.interruptionManager = InterruptionManagerV2(self.handler_data)


    def tearDown(self):
        pass


    def testName(self):
        self.assertTrue(True)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()