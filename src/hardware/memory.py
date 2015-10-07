class Memory:

    def __init__(self):
        self.memory = {}
        self.direction = 0

    def put(self, instruction):

        self.memory[self.direction] = instruction
        self.direction = self.direction + 1

    def get(self, direction):

        return self.memory[direction]

