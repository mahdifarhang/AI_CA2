

INFINITY = 10000

class Agent:
    def __init__(self, color, opponentColor, time=None, height = 5):
        self.color = color
        self.opponentColor = opponentColor
        self.height = height


    def move(self, board):
        before = board.travelOverBoard(self.color)
        val, from_cell, to_cell = minimax(board, 0, self.height, True, self.color, self.opponentColor, -INFINITY, INFINITY)
        after = board.travelOverBoard(self.color)
        print(val)
        return from_cell, to_cell


def distances(board, color):
    pieces = board.travelOverBoard(color)
    result = 0
    for piece in pieces:
        if (color == 'W'):
            result += (piece[0] + 1) * (piece[0] + 1)
        else:
            result += (6 - piece[0]) * (6 - piece[0])
    return result


def eval_func(board, color, enemy_color):
    return distances(board, enemy_color) - distances(board, color)


def minimax(board, depth, height, is_maximizer, color, enemy_color, alpha, beta):
    from_ = (-1, -1)
    to_ = (-1, -1)
    if (is_maximizer):
        if (board.win(color)):
            return INFINITY, from_, to_
        if (depth >= height):
            return eval_func(board, color, enemy_color), from_, to_
        best_val = -INFINITY
        for i in range(board.n_rows):
            for j in range(board.n_cols):
                if (board.board[i][j] == color):
                    destinations = board.getPiecePossibeLocations(color, i, j)
                    for destination in destinations:
                        before_move = board.board[destination[0]][destination[1]]
                        board.changePieceLocation(color, (i, j), destination)
                        value, a, b = minimax(board, depth + 1, height, False, color, enemy_color, alpha, beta)
                        board.changePieceLocation(color, destination, (i, j))
                        board.board[destination[0]][destination[1]] = before_move
                        if (value > best_val):
                            best_val = value
                            from_ = (i, j)
                            to_ = destination
                        alpha = max(alpha, best_val)
                        if (beta <= alpha):
                            return best_val, from_, to_

    else:
        if (board.win(enemy_color)):
            return -INFINITY, from_, to_
        if (depth >= height):
            return eval_func(board, enemy_color, color), from_, to_
        best_val = INFINITY
        for i in range(board.n_rows):
            for j in range(board.n_cols):
                if (board.board[i][j] == enemy_color):
                    destinations = board.getPiecePossibeLocations(enemy_color, i, j)
                    for destination in destinations:
                        before_move = board.board[destination[0]][destination[1]]
                        board.changePieceLocation(enemy_color, (i, j), destination)
                        value, a, b = minimax(board, depth + 1, height, True, color, enemy_color, alpha, beta)
                        board.changePieceLocation(enemy_color, destination, (i, j))
                        board.board[destination[0]][destination[1]] = before_move
                        if (value < best_val):
                            best_val = value
                            from_ = (i, j)
                            to_ = destination
                        best_val = min(best_val, value)
                        beta = min(beta, best_val)
                        if (beta <= alpha):
                            return best_val, from_, to_
    return best_val, from_, to_
