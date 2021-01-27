import keyboard
from flask import get_template_attribute

class Snake:
    def __init__(self, head):
        self.parts = []
        self.length = 1

        self.grow(head)

        keyboard.add_hotkey('w', self.go_up)
        keyboard.add_hotkey('a', self.go_left)
        keyboard.add_hotkey('d', self.go_right)
        keyboard.add_hotkey('s', self.go_down)

    def grow(self, part):
        self.parts.append(part)

    def get_length(self):
        return self.length

    def get_head(self):
        return self.parts[0]

    def go_up(self):
        self.parts[0][0] += 1
        self.parts[0][1] += 1

        print('Head at', self.parts[0][0], self.parts[0][1])

    def go_left(self):
        pass

    def go_right(self):
        pass

    def go_down(self):
        pass

class Part:
    def __init__(self):
        pass