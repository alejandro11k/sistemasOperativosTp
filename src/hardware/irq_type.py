
from enum import Enum

class IrqType(Enum):
    irqKILL = 1
    irqIO = 2
    irqEND_IO = 3
    irqTIME_OUT = 4
    irqNEW = 5
    irqIOfromCPU = 6
    irqIOfromIO = 7
    irqProcess = 8