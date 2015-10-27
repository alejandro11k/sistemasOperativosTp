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

    