class Memory:

    def __init__(self):
        self.memory = {}
        self.firstFreeDirection = 0

    def put(self, instruction):

        self.memory[self.firstFreeDirection] = instruction
        self.direction = self.firstFreeDirection + 1

    def get(self, direction):

        return self.memory[direction]

