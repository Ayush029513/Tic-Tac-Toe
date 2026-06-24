class Game:
    def __init__(self):
        self.board = [" "] * 9

    def make_move(self, pos, player):
        if self.board[pos] == " ":
            self.board[pos] = player
            return True
        return False

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def winner(self):
        wins = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        for combo in wins:
            a,b,c = combo
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]

        if " " not in self.board:
            return "Draw"

        return None