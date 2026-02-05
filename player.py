class Player:
    def __init__(self, name, color, start_pos):
        self.name = name
        self.color = color
        self.position = start_pos
        self.start_pos = start_pos

    def move(self, steps):
        self.position += steps
        if self.position > 56:
            self.position = 56

    def reset(self):
        self.position = self.start_pos
