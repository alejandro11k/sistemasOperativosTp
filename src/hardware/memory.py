class Memory:

    def __init__(self):
        self.memory = {}

    def put(self, direction, instruction):

        self.memory[direction] = instruction

    def get(self, direction):

        return self.memory[direction]
