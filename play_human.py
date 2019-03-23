from agent import Agent
from board import Board
from graphicalBoard import GraphicalBoard


def switchTurn(turn):
    if turn == 'W':
        return 'B'
    return 'W'


def play(white, black, board):
    graphicalBoard = GraphicalBoard(board)
    turn = 'W'
    while not board.finishedGame():
        if turn == 'W':
            from_cell, to_cell = white.move(board)
        elif turn == 'B':
            from_cell, to_cell = black.move(board)
        else:
            raise Exception
        board.changePieceLocation(turn, from_cell, to_cell)
        turn = switchTurn(turn)
        graphicalBoard.showBoard()




class Human:
    def __init__(self, color, opponentColor, time=None, height = 5):
        self.color = color
        self.opponentColor = opponentColor
        self.height = height


    def move(self, board):
        m = input()
        b = int(m[0])
        a = int(m[1])
        d = int(m[2])
        c = int(m[3])
        from_ = (a - 1, b - 1)
        to_ = (c - 1, d - 1)
        return from_, to_

if __name__ == '__main__':
    board = Board(6, 6, 2)
    white = Human('W', 'B')
    you = Agent('B', 'W')
    play(white, you, board)
