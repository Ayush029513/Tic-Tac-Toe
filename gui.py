import tkinter as tk
from tkinter import messagebox

from game import Game
from ai import best_move


class TicTacToeGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("AI Tic-Tac-Toe")

        self.game = Game()

        self.buttons = []

        for i in range(9):
            button = tk.Button(
                self.root,
                text="",
                width=8,
                height=4,
                font=("Arial", 20),
                command=lambda i=i: self.player_move(i)
            )

            button.grid(row=i//3, column=i%3)

            self.buttons.append(button)

    def player_move(self, pos):

        if self.game.make_move(pos, "X"):
            self.update_board()

            result = self.game.winner()

            if result:
                self.end_game(result)
                return

            ai_pos = best_move(self.game)

            if ai_pos is not None:
                self.game.make_move(ai_pos, "O")

            self.update_board()

            result = self.game.winner()

            if result:
                self.end_game(result)

    def update_board(self):

        for i in range(9):
            self.buttons[i]["text"] = self.game.board[i]

    def end_game(self, result):

        messagebox.showinfo("Game Over", f"Result: {result}")
        self.root.destroy()

    def run(self):
        self.root.mainloop()