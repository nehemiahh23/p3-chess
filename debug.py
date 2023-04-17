#!/usr/bin/env python3
from lib.classes.pawn import Pawn

if __name__ == '__main__':
    pa2 = Pawn([1, 0])

    board = [[None, None], [pa2, None]]

    def print_board():
        for row in board:
            print(row)

    def swapPositions(inp1, inp2):
        board[inp1[0]][inp1[1]], board[inp2[0]][inp2[1]] = board[inp2[0]][inp2[1]], board[inp1[0]][inp1[1]]
        print(board[0])
        print(board[1])

    def get_index():
        for row in board:
            for sq in row:
                if sq == pa2:
                    return [board.index(row), row.index(sq)]