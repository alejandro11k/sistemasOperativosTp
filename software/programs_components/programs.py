from software.programs_components.program import Program
from software.programs_components.instruction import Instruction
from software.programs_components.instruction_type import InstructionType

class Programs:

    def __init__(self):
        self.instructions = {}
        self.programs = []
        self.initialize()
    
    def initialize(self):
        self.addInstructions()
        self.addPrograms()
        
    def addPrograms(self):
        self.cpuProgram()
        self.inProgram()
        self.outProgram()
        self.longCpuProgram()
        self.realImputProgram()
        self.longProgram()
            
    def addInstructions(self):
        instructionEnd = Instruction(InstructionType.instructionEND,"END")
        instructionCpu = Instruction(InstructionType.instructionCPU,"CPU")
        instructionCpuJump = Instruction(InstructionType.instructionCPU,"JUMP0")
        instructionPrint = Instruction(InstructionType.instructionIO,"PRINT")
        instructionInput = Instruction(InstructionType.instructionIO,"INPUT")
        instructionRealInput = Instruction(InstructionType.instructionIO,"realINPUT")
        
        
        self.instructions['END'] = instructionEnd
        self.instructions['CPU'] = instructionCpu
        self.instructions['PRINT'] = instructionPrint
        self.instructions['INPUT'] = instructionInput
        self.instructions['realINPUT'] = instructionRealInput
        self.instructions['JUMP0'] = instructionCpuJump
    
    def realImputProgram(self):
        
        instructions = []
        instructions.append(self.instructions['realINPUT'])
        instructions.append(self.instructions['JUMP0'])
        instructions.append(self.instructions['END'])
        
        program = Program("realINPUT")
        program.compileInstructions(instructions)
        
        self.programs.append(program)
        
    def cpuProgram(self):
        
        instructions = []
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions['END'])
        
        program = Program("empty_program")
        program.compileInstructions(instructions)
        
        self.programs.append(program)
        
    def longCpuProgram(self):
        
        instructions = []
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions['END'])
        
        program = Program("empty_program2")
        program.compileInstructions(instructions)
        
        self.programs.append(program)
        
    def longProgram(self):
        
        instructions = []
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions["PRINT"])
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions["INPUT"])
        instructions.append(self.instructions["PRINT"])
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions["PRINT"])
        instructions.append(self.instructions["INPUT"])
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions["INPUT"])
        instructions.append(self.instructions['END'])
        
        program = Program("long")
        program.compileInstructions(instructions)
        
        self.programs.append(program)
        
    def outProgram(self):
        
        instructions = []
        instructions.append(self.instructions["CPU"])
        instructions.append(self.instructions["PRINT"])
        instructions.append(self.instructions["END"])
        
        program = Program("io_program")
        program.compileInstructions(instructions)
        
        self.programs.append(program)
        
        
    def inProgram(self):
        instructions = []
        instructions.append(self.instructions["CPU"])
        instructions.append(self.instructions["INPUT"])
        instructions.append(self.instructions["END"])
        
        program = Program("io_program2")
        program.compileInstructions(instructions)
        
        self.programs.append(program)