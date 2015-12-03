class Memory:

    def __init__(self):
        self.memory = {}
        self.firstFreeDirection = 0

    def put(self, instruction):

        self.memory[self.firstFreeDirection] = instruction
        self.firstFreeDirection = self.firstFreeDirection + 1

    def get(self, direction):

        value = self.memory[direction]
        return value

class LimitedMemory(Memory):
    
    def __init__(self,blocks):
        Memory.__init__(self)
        self.blocks = blocks-1
        
    def ilegalAdrress(self,address):
        return address>self.blocks
        
    def size(self):
        return self.blocks
    
    def put(self, address,instruction):

        if self.ilegalAdrress(address):
            print("OUT OF MEMORY")
        else:
            self.memory[address] = instruction
            
    