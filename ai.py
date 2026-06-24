from game import Game

def minimax(game, maximizing):

    result = game.winner()

    if result == "X":
        return 1
    elif result == "O":
        return -1
    elif result == "Draw":
        return 0

    if maximizing:
        best = -100

        for move in game.available_moves():
            game.board[move] = "X"
            score = minimax(game, False)
            game.board[move] = " "
            best = max(best, score)

        return best

    else:
        best = 100

        for move in game.available_moves():
            game.board[move] = "O"
            score = minimax(game, True)
            game.board[move] = " "
            best = min(best, score)

        return best


def best_move(game):

    best_score = 100
    move_choice = None

    for move in game.available_moves():
        game.board[move] = "O"
        score = minimax(game, True)
        game.board[move] = " "

        if score < best_score:
            best_score = score
            move_choice = move

    return move_choice