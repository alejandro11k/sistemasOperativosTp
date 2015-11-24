from software.programs_components.program import Program
from software.programs_components.instruction import Instruction
from software.programs_components.instruction import RealInstruction
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
        self.realInProgram()
            
    def addInstructions(self):
        instructionEnd = Instruction(InstructionType.instructionEND,"END")
        instructionCpu = Instruction(InstructionType.instructionCPU,"CPU")
        instructionPrint = Instruction(InstructionType.instructionIO,"PRINT")
        instructionInput = Instruction(InstructionType.instructionIO,"INPUT")
        instructionRealInput = RealInstruction(InstructionType.instructionIO,"realINPUT")
        
        self.instructions['END'] = instructionEnd
        self.instructions['CPU'] = instructionCpu
        self.instructions['PRINT'] = instructionPrint
        self.instructions['INPUT'] = instructionInput
        self.instructions['realINPUT'] = instructionRealInput
    
    def cpuProgram(self):
        
        instructions = []
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions['CPU'])
        instructions.append(self.instructions['END'])
        
        program = Program("empty")
        program.compileInstructions(instructions)
        
        self.programs.append(program)
        
        
    def outProgram(self):
        
        instructions = []
        instructions.append(self.instructions["CPU"])
        instructions.append(self.instructions["PRINT"])
        instructions.append(self.instructions["END"])
        
        program = Program("io01")
        program.compileInstructions(instructions)
        
        self.programs.append(program)
        
        
    def inProgram(self):
        instructions = []
        instructions.append(self.instructions["CPU"])
        instructions.append(self.instructions["INPUT"])
        instructions.append(self.instructions["END"])
        
        program = Program("io02")
        program.compileInstructions(instructions)
        
        self.programs.append(program)
        
    def realInProgram(self):
        instructions = []
        instructions.append(self.instructions["realINPUT"])
        instructions.append(self.instructions["realINPUT"])
        instructions.append(self.instructions["realINPUT"])
        instructions.append(self.instructions["realINPUT"])
        instructions.append(self.instructions["CPU"])
        instructions.append(self.instructions["END"])
        
        program = Program("realInput")
        program.compileInstructions(instructions)
        
        self.programs.append(program)