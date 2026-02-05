import tkinter as tk
from config import CELL_SIZE, GRID_SIZE

class Board:
    def __init__(self, canvas):
        self.canvas = canvas
        self.draw_grid()

    def draw_grid(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x1 = i * CELL_SIZE
                y1 = j * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")

    def draw_token(self, position, color):
        row = position % GRID_SIZE
        col = position // GRID_SIZE

        x1 = row * CELL_SIZE + 10
        y1 = col * CELL_SIZE + 10
        x2 = x1 + CELL_SIZE - 20
        y2 = y1 + CELL_SIZE - 20

        self.canvas.create_oval(x1, y1, x2, y2, fill=color)
