class Snake:
    def __init__(self):
        self.parts = []
        self.length = 1

        self.grow()

    def grow(self):
        self.parts.append(Part())

    def get_length(self):
        return self.length

class Part:
    def __init__(self):
        pass