from minimax import Minimax
from tree import Tree


class Agent:
    def __init__(self, color, opponentColor, time=None):
        self.color = color
        self.opponentColor = opponentColor
        self.height = 3


    # def move(self):
        # todo: you have to implement this agent.
        # ...
        # return from_cell, to_cell

    def move(self, board):
        gameTree = Tree(board, self.color, self.opponentColor, self.height)
        from_cell, to_cell = Minimax.calNextMove(gameTree, self.height)
        return from_cell, to_cell
