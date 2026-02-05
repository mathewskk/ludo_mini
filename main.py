import tkinter as tk
from board import Board
from player import Player
from dice import roll_dice
from config import WINDOW_SIZE, PLAYERS

class LudoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Ludo")

        self.canvas = tk.Canvas(root, width=WINDOW_SIZE, height=WINDOW_SIZE)
        self.canvas.pack()

        self.board = Board(self.canvas)

        self.players = [
            Player("Player 1", "red", 0),
            Player("Player 2", "blue", 0)
        ]

        self.current_player = 0

        self.roll_button = tk.Button(root, text="Roll Dice", command=self.play_turn)
        self.roll_button.pack()

        self.info_label = tk.Label(root, text="Player 1 Turn")
        self.info_label.pack()

        self.update_board()

    def play_turn(self):
        dice_value = roll_dice()

        player = self.players[self.current_player]
        player.move(dice_value)

        self.info_label.config(
            text=f"{player.name} rolled {dice_value}"
        )

        self.current_player = (self.current_player + 1) % len(self.players)
        self.update_board()

    def update_board(self):
        self.canvas.delete("all")
        self.board.draw_grid()

        for player in self.players:
            self.board.draw_token(player.position, player.color)

def main():
    root = tk.Tk()
    game = LudoGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
