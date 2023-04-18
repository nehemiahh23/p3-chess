#!/usr/bin/env python3
from lib.classes.pawn import Pawn
from lib.classes.rook import Rook
from lib.classes.knight import Knight
from lib.classes.bishop import Bishop
from lib.classes.queen import Queen
from lib.classes.king import King

if __name__ == '__main__':
    ra8 = Rook([0, 0], black=True)
    nb8 = Knight([0, 1], black=True)
    bc8 = Bishop([0, 2], black=True)
    qd8 = Queen([0, 3], black=True)
    ke8 = King([0, 4], black=True)
    bf8 = Bishop([0, 5], black=True)
    ng8 = Knight([0, 6], black=True)
    rh8 = Rook([0, 7], black=True)

    pa7 = Pawn([1, 0], black=True)
    pb7 = Pawn([1, 1], black=True)
    pc7 = Pawn([1, 2], black=True)
    pd7 = Pawn([1, 3], black=True)
    pe7 = Pawn([1, 4], black=True)
    pf7 = Pawn([1, 5], black=True)
    pg7 = Pawn([1, 6], black=True)
    ph7 = Pawn([1, 7], black=True)

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

    board = [[ra8, nb8, bc8, qd8, ke8, bf8, ng8, rh8], [pa7, pb7, pc7, pd7, pe7, pf7, pg7, ph7], ["□", "□", "□", "□", "□", "□", "□", "□"], ["□", "□", "□", "□", "□", "□", "□", "□"], ["□", "□", "□", "□", "□", "□", "□", "□"], ["□", "□", "□", "□", "□", "□", "□", "□"], [pa2, pb2, pc2, pd2, pe2, pf2, pg2, ph2], [ra1, nb1, bc1, qd1, ke1, bf1, ng1, rh1]]

    def print_board():
        for row in board:
            print(row)

    def swap_positions(inp1, inp2):
        def move():
            board[inp1[0]][inp1[1]], board[inp2[0]][inp2[1]] = board[inp2[0]][inp2[1]], board[inp1[0]][inp1[1]] # movement
            board[inp2[0]][inp2[1]].pos = inp2
            board[inp2[0]][inp2[1]].calc()
            print_board()
        pos_exists = False
        pos_vacant = False
        # print(range(inp1[1] + 1, inp2[1]), -1)
        for num in range(inp1[1] + 1, inp2[1]):
            print(num)
        
        if 0 <= inp2[0] <= 7 and 0 <= inp2[1] <= 7: # checks if desired position is on the board
            pos_exists = True
        else:
            print("position invalid")
        if board[inp2[0]][inp2[1]] != "□": # checks if desired position is vacant
                if board[inp1[0]][inp1[1]].black == board[inp2[0]][inp2[1]].black: # team check for capt
                    print("position occupied")
                else:
                    board[inp2[0]][inp2[1]].cptd = True
                    pos_vacant = True
        else:
            pos_vacant = True
        if pos_exists and pos_vacant:
            if isinstance(board[inp1[0]][inp1[1]], Pawn): # pawn collision (1st move)
                if inp2 == board[inp1[0]][inp1[1]].n2_pos:
                    if board[inp1[0] - 1][inp1[1]] != "□":
                        print("position blocked")
                    else:
                        move()
                else:
                    move()
            elif isinstance(board[inp1[0]][inp1[1]], Rook): # rook collision
                r_row_range = range(inp1[1] + 1, inp2[1]) if inp1[1] < inp2[1] else range(inp1[1], inp2[1], -1)
                r_col_range = range(inp1[0] - 1, inp2[0]) if inp1[0] < inp2[0] else range(inp1[0] - 1, inp2[0], -1)
                print(r_col_range)
                if inp2[1] == inp1[1] + 1 or inp2[1] == inp1[1] - 1: # horizontal
                    move()
                else:
                    blocked = True
                    for col in r_row_range: 
                        print(col)
                        if board[inp1[0]][col] != "□":
                            print("position blocked")
                            board[inp2[0]][inp2[1]].cptd = False
                        else:
                            blocked = False
                    if not blocked:
                        move()
                            # return None
                
                if inp2[0] == inp1[0] + 1 or inp2[0] == inp1[0] - 1: # vertical
                    move()
                else:
                    blocked = True
                    for row in r_col_range:
                        print(board[row][inp1[1]])
                        if board[row][inp1[1]] != "□":
                            print("position blocked")
                            board[inp2[0]][inp2[1]].cptd = False
                            return None
                        else:
                            blocked = False
                    if not blocked:
                        move()

            elif isinstance(board[inp1[0]][inp1[1]], Knight): # bishop collision
                move()
            elif isinstance(board[inp1[0]][inp1[1]], King): # bishop collision
                move()
            elif isinstance(board[inp1[0]][inp1[1]], Bishop): # bishop collision
                move()
            elif isinstance(board[inp1[0]][inp1[1]], Queen): # queen collision
                move()

    def get_index():
        for row in board:
            for sq in row:
                if sq == pa2:
                    return [board.index(row), row.index(sq)]
