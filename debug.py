#!/usr/bin/env python3
from lib.classes.pawn import Pawn
from lib.classes.rook import Rook
from lib.classes.knight import Knight
from lib.classes.bishop import Bishop
from lib.classes.queen import Queen
from lib.classes.king import King

if __name__ == '__main__':
    ra8 = Rook([0, 0])
    nb8 = Knight([0, 1])
    bc8 = Bishop([0, 2])
    qd8 = Queen([0, 3])
    ke8 = King([0, 4])
    bf8 = Bishop([0, 5])
    ng8 = Knight([0, 6])
    rh8 = Rook([0, 7])

    pa7 = Pawn([1, 0])
    pb7 = Pawn([1, 1])
    pc7 = Pawn([1, 2])
    pd7 = Pawn([1, 3])
    pe7 = Pawn([1, 4])
    pf7 = Pawn([1, 5])
    pg7 = Pawn([1, 6])
    ph7 = Pawn([1, 7])

    pa2 = Pawn([6, 0])
    pb2 = Pawn([6, 1])
    pc2 = Pawn([6, 2])
    pd2 = Pawn([6, 3])
    pe2 = Pawn([6, 4])
    pf2 = Pawn([6, 5])
    pg2 = Pawn([6, 6])
    ph2 = Pawn([6, 7])

    ra1 = Rook([7, 0])
    nb1 = Knight([7, 1])
    bc1 = Bishop([7, 2])
    qd1 = Queen([7, 3])
    ke1 = King([7, 4])
    bf1 = Bishop([7, 5])
    ng1 = Knight([7, 6])
    rh1 = Rook([7, 7])

    board = [[ra8, nb8, bc8, qd8, ke8, bf8, ng8, rh8], [pa7, pb7, pc7, pd7, pe7, pf7, pg7, ph7], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [pa2, pb2, pc2, pd2, pe2, pf2, pg2, ph2], [ra1, nb1, bc1, qd1, ke1, bf1, ng1, rh1]]

    def print_board():
        for row in board:
            print(row)

    def swap_positions(inp1, inp2):
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
