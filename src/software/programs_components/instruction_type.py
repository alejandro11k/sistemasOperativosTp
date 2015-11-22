from enum import Enum

class InstructionType(Enum):
    instructionCPU = 1
    instructionIO = 2
    instructionEND = 0