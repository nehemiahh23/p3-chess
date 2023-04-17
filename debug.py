#!/usr/bin/env python3
from lib.classes.pawn import Pawn

if __name__ == '__main__':
    pa2 = Pawn([1, 0])
    pb2 = Pawn([1, 1])

    board = [[None, None], [pa2, pb2]]

    def print_board():
        for row in board:
            print(row)

    def swapPositions(inp1, inp2):
        if 0 <= inp2[0] <= 1 and 0 <= inp2[1] <= 1: # checks if desired position is on the board
            print("position valid, checking vacancy")
            if board[inp2[0]][inp2[1]] == None: # checks if desired position is vacant (will be tweaked to check for team later)
                print("position vacant, moving")
                board[inp1[0]][inp1[1]], board[inp2[0]][inp2[1]] = board[inp2[0]][inp2[1]], board[inp1[0]][inp1[1]]
                board[inp2[0]][inp2[1]].pos = inp2
                print(board[0])
                print(board[1])
            else:
                print("position occupied")
        else:
            print("position invalid")

    def get_index():
        for row in board:
            for sq in row:
                if sq == pa2:
                    return [board.index(row), row.index(sq)]
