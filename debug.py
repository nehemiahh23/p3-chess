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
            print(' '.join([str(elem) for elem in row]))

    def swap_positions(inp1, inp2):
        def move():
            board[inp1[0]][inp1[1]].pos = inp2
            board[inp1[0]][inp1[1]].calc()
            board[inp1[0]][inp1[1]], board[inp2[0]][inp2[1]] = board[inp2[0]][inp2[1]], board[inp1[0]][inp1[1]] # movement
            print_board()
        pos_exists = False
        pos_vacant = False
        blocked = True
        
        if 0 <= inp2[0] <= 7 and 0 <= inp2[1] <= 7: # checks if desired position is on the board
            pos_exists = True
        else:
            print("Move Invalid")
        if board[inp2[0]][inp2[1]] != "□": # checks if desired position is vacant
                if board[inp1[0]][inp1[1]].black == board[inp2[0]][inp2[1]].black: # team check for capt
                    print("Move Invalid")
                else:
                    pos_vacant = True
        else:
            pos_vacant = True
        if pos_exists and pos_vacant:
            if isinstance(board[inp1[0]][inp1[1]], Pawn): # pawn collision (1st move)
                if hasattr(board[inp1[0]][inp1[1]], "n2_pos") and inp2 == board[inp1[0]][inp1[1]].n2_pos:
                    if board[inp1[0] - 1][inp1[1]] != "□":
                        print("Move Invalid")
                    else:
                        move()
                elif hasattr(board[inp1[0]][inp1[1]], "s2_pos") and inp2 == board[inp1[0]][inp1[1]].s2_pos:
                    if board[inp1[0] + 1][inp1[1]] != "□":
                        print("Move Invalid")
                    else:
                        move()
                else:
                    move()
            
            elif isinstance(board[inp1[0]][inp1[1]], Rook): # rook collision
                if inp1[1] < inp2[1]: # if move right (if start col < end col)
                    if [inp2[0], inp2[1]] in board[inp1[0]][inp1[1]].positions[1]:
                        if inp1[1] + 1 == inp2[1]: # if its moving 1 square
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                    board[inp2[0]][inp2[1]].cptd = True
                            move()
                        else: # if its moving more than 1 square
                            piece_inst = board[inp1[0]][inp1[1]]
                            arr = piece_inst.positions[1]
                            desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                            for pos in arr[slice(arr.index(desired_pos))]:
                                if board[pos[0]][pos[1]] != "□":
                                    print("Move Invalid")
                                    return
                                else:
                                    blocked = False

                            if not blocked:
                                if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                    board[inp2[0]][inp2[1]].cptd = True
                                move()
                    else:
                        print("Move Invalid")
                elif inp1[1] > inp2[1]: # if move left (if start col > end col)
                    if [inp2[0], inp2[1]] in board[inp1[0]][inp1[1]].positions[3]:
                        if inp1[1] - 1 == inp2[1]: # if its moving 1 square
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                    board[inp2[0]][inp2[1]].cptd = True
                            move()
                        else: # if its moving more than 1 square
                            piece_inst = board[inp1[0]][inp1[1]]
                            arr = piece_inst.positions[3]
                            desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                            for pos in arr[slice(arr.index(desired_pos))]:
                                if board[pos[0]][pos[1]] != "□":
                                    print("Move Invalid")
                                    return
                                else:
                                    blocked = False

                            if not blocked:
                                if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                    board[inp2[0]][inp2[1]].cptd = True
                                move()
                    else:
                        print("Move Invalid")
                elif inp1[0] > inp2[0]: # if move up (if start row > end row)
                    if [inp2[0], inp2[1]] in board[inp1[0]][inp1[1]].positions[0]:
                        if inp1[0] - 1 == inp2[0]: # if its moving 1 square
                            blocked = False
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                    board[inp2[0]][inp2[1]].cptd = True
                            move()
                        else: # if its moving more than 1 square
                            piece_inst = board[inp1[0]][inp1[1]]
                            arr = piece_inst.positions[0]
                            desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                            for pos in arr[slice(arr.index(desired_pos))]:
                                if board[pos[0]][pos[1]] != "□":
                                    print("Move Invalid")
                                    return
                                else:
                                    blocked = False

                            if not blocked:
                                if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                    board[inp2[0]][inp2[1]].cptd = True
                                move()
                    else:
                        print("Move Invalid")
                elif inp1[0] < inp2[0]: # if move down (if start row < end row)
                    if [inp2[0], inp2[1]] in board[inp1[0]][inp1[1]].positions[1]:
                        if inp1[0] + 1 == inp2[0]: # if its moving 1 square
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                    board[inp2[0]][inp2[1]].cptd = True
                            move()
                        else: # if its moving more than 1 square
                            piece_inst = board[inp1[0]][inp1[1]]
                            arr = piece_inst.positions[2]
                            desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                            for pos in arr[slice(arr.index(desired_pos))]:
                                if board[pos[0]][pos[1]] != "□":
                                    print("Move Invalid")
                                    # if hasattr(board[inp2[0]][inp2[1]], "ctpd"):
                                    #     board[inp2[0]][inp2[1]].cptd = False
                                    return
                                else:
                                    blocked = False

                            if not blocked:
                                if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                    board[inp2[0]][inp2[1]].cptd = True
                                move()
                    else:
                        print("Move Invalid")

            elif isinstance(board[inp1[0]][inp1[1]], Bishop): # bishop collision
                if inp1[0] > inp2[0] and inp1[1] < inp2[1]: # if move ne (row > row, col < col)
                    if inp1[0] - 1 == inp2[0] and inp1[1] + 1 == inp2[1]:
                        if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                        move()
                    else:
                        piece_inst = board[inp1[0]][inp1[1]]
                        arr = piece_inst.positions[0]
                        desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                        for pos in arr[slice(arr.index(desired_pos))]:
                            if board[pos[0]][pos[1]] != "□":
                                print("Move Invalid")
                                return
                            else:
                                blocked = False

                        if not blocked:
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                            move()
                elif inp1[0] < inp2[0] and inp1[1] < inp2[1]: # if move se (row < row, col < col)
                    if inp1[0] + 1 == inp2[0] and inp1[1] + 1 == inp2[1]:
                        if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                        move()
                    else:
                        piece_inst = board[inp1[0]][inp1[1]]
                        arr = piece_inst.positions[1]
                        desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                        for pos in arr[slice(arr.index(desired_pos))]:
                            if board[pos[0]][pos[1]] != "□":
                                print("Move Invalid")
                                return
                            else:
                                blocked = False

                        if not blocked:
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                            move()
                elif inp1[0] < inp2[0] and inp1[1] > inp2[1]: # if move sw (row > row, col < col)
                    if inp1[0] + 1 == inp2[0] and inp1[1] - 1 == inp2[1]:
                        if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                        move()
                    else:
                        piece_inst = board[inp1[0]][inp1[1]]
                        arr = piece_inst.positions[2]
                        desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                        for pos in arr[slice(arr.index(desired_pos))]:
                            if board[pos[0]][pos[1]] != "□":
                                print("Move Invalid")
                                return
                            else:
                                blocked = False

                        if not blocked:
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                            move()
                elif inp1[0] > inp2[0] and inp1[1] > inp2[1]: # if move nw (row > row, col < col)
                    if inp1[0] - 1 == inp2[0] and inp1[1] - 1 == inp2[1]:
                        if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                        move()
                    else:
                        piece_inst = board[inp1[0]][inp1[1]]
                        arr = piece_inst.positions[3]
                        desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                        for pos in arr[slice(arr.index(desired_pos))]:
                            if board[pos[0]][pos[1]] != "□":
                                print("Move Invalid")
                                return
                            else:
                                blocked = False

                        if not blocked:
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                            move()


            elif isinstance(board[inp1[0]][inp1[1]], Queen): # queen collision
                if inp1[1] < inp2[1] and inp1[0] == inp2[0]: # if move right (if start col < end col)
                    if inp1[1] + 1 == inp2[1]: # if its moving 1 square
                        if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                        move()
                    else: # if its moving more than 1 square
                        piece_inst = board[inp1[0]][inp1[1]]
                        arr = piece_inst.positions[2]
                        desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                        for pos in arr[slice(arr.index(desired_pos))]:
                            if board[pos[0]][pos[1]] != "□":
                                print("Move Invalid")
                                return
                            else:
                                blocked = False

                        if not blocked:
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                            move()
                elif inp1[1] > inp2[1] and inp1[0] == inp2[0]: # if move left (if start col > end col)
                    if inp1[1] - 1 == inp2[1]: # if its moving 1 square
                        if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                        move()
                    else: # if its moving more than 1 square
                        piece_inst = board[inp1[0]][inp1[1]]
                        arr = piece_inst.positions[6]
                        desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                        for pos in arr[slice(arr.index(desired_pos))]:
                            if board[pos[0]][pos[1]] != "□":
                                print("Move Invalid")
                                return
                            else:
                                blocked = False

                        if not blocked:
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                            move()
                elif inp1[0] > inp2[0] and inp1[1] == inp2[1]: # if move up (if start row > end row)
                    if inp1[0] - 1 == inp2[0]: # if its moving 1 square
                        blocked = False
                        if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                        move()
                    else: # if its moving more than 1 square
                        piece_inst = board[inp1[0]][inp1[1]]
                        arr = piece_inst.positions[0]
                        desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                        for pos in arr[slice(arr.index(desired_pos))]:
                            if board[pos[0]][pos[1]] != "□":
                                print("Move Invalid")
                                return
                            else:
                                blocked = False

                        if not blocked:
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                            move()
                elif inp1[0] < inp2[0] and inp1[1] == inp2[1]: # if move down (if start row < end row)
                    if inp1[0] + 1 == inp2[0]: # if its moving 1 square
                        if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                        move()
                    else: # if its moving more than 1 square
                        piece_inst = board[inp1[0]][inp1[1]]
                        arr = piece_inst.positions[4]
                        desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                        for pos in arr[slice(arr.index(desired_pos))]:
                            if board[pos[0]][pos[1]] != "□":
                                print("Move Invalid")
                                # if hasattr(board[inp2[0]][inp2[1]], "ctpd"):
                                #     board[inp2[0]][inp2[1]].cptd = False
                                return
                            else:
                                blocked = False

                        if not blocked:
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                            move()
                elif inp1[0] > inp2[0] and inp1[1] < inp2[1]: # if move ne (row > row, col < col)
                    if inp1[0] - 1 == inp2[0] and inp1[1] + 1 == inp2[1]:
                        if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                        move()
                    else:
                        piece_inst = board[inp1[0]][inp1[1]]
                        arr = piece_inst.positions[1]
                        desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                        for pos in arr[slice(arr.index(desired_pos))]:
                            if board[pos[0]][pos[1]] != "□":
                                print("Move Invalid")
                                return
                            else:
                                blocked = False

                        if not blocked:
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                            move()
                elif inp1[0] < inp2[0] and inp1[1] < inp2[1]: # if move se (row < row, col < col)
                    if inp1[0] + 1 == inp2[0] and inp1[1] + 1 == inp2[1]:
                        if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                        move()
                    else:
                        piece_inst = board[inp1[0]][inp1[1]]
                        arr = piece_inst.positions[3]
                        desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                        for pos in arr[slice(arr.index(desired_pos))]:
                            if board[pos[0]][pos[1]] != "□":
                                print("Move Invalid")
                                return
                            else:
                                blocked = False

                        if not blocked:
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                            move()
                elif inp1[0] < inp2[0] and inp1[1] > inp2[1]: # if move sw (row > row, col < col)
                    if inp1[0] + 1 == inp2[0] and inp1[1] - 1 == inp2[1]:
                        if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                        move()
                    else:
                        piece_inst = board[inp1[0]][inp1[1]]
                        arr = piece_inst.positions[5]
                        desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                        for pos in arr[slice(arr.index(desired_pos))]:
                            if board[pos[0]][pos[1]] != "□":
                                print("Move Invalid")
                                return
                            else:
                                blocked = False

                        if not blocked:
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                            move()
                elif inp1[0] > inp2[0] and inp1[1] > inp2[1]: # if move nw (row > row, col < col)
                    if inp1[0] - 1 == inp2[0] and inp1[1] - 1 == inp2[1]:
                        if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                        move()
                    else:
                        piece_inst = board[inp1[0]][inp1[1]]
                        arr = piece_inst.positions[7]
                        desired_pos = [pos for pos in arr if pos == [inp2[0], inp2[1]]][0]
                        for pos in arr[slice(arr.index(desired_pos))]:
                            if board[pos[0]][pos[1]] != "□":
                                print("Move Invalid")
                                # this one
                                return
                            else:
                                blocked = False

                        if not blocked:
                            if hasattr(board[inp2[0]][inp2[1]], "cptd"):
                                board[inp2[0]][inp2[1]].cptd = True
                            move()



            elif isinstance(board[inp1[0]][inp1[1]], Knight): # bishop collision
                move()

            elif isinstance(board[inp1[0]][inp1[1]], King): # bishop collision
                move()


    def get_index():
        for row in board:
            for sq in row:
                if sq == pa2:
                    return [board.index(row), row.index(sq)]





class CLI:

    def __init__(self,team="white"):
        self.team = team
        self.welcome()
        self.rules()
        self.turn()

    def welcome(self):
        print("/////////Welcome to Capture the King/////////// \n An 'Original Game' created by Steven & Nehemiah")

    def rules(self):
        print("//////The Rules///////// \n 1. The aim of the game is to capture the opposition's king (there is no check or checkmate so don't get caught 'sleeping') \n 2. The pieces move the exact same way as chess pieces (except there is no castling or en passant)")
        print_board()
        
    def turn(self):
        while input != "King has been caught":

            print("Where is the piece you would like to move?")
            input_start_cords = input()
            arr = []
            for char in input_start_cords:
                if char == '1':
                    arr.append(7)
                elif char == '2':
                    arr.append(6)
                elif char == '3':
                    arr.append(5)
                elif char == '4':
                    arr.append(4)
                elif char == '5':
                    arr.append(3)
                elif char == '6':
                    arr.append(2)
                elif char == '7':
                    arr.append(1)
                elif char == '8':
                    arr.append(0)
                elif char == 'a':
                    arr.append(0)
                elif char == 'b':
                    arr.append(1)
                elif char == 'c':
                    arr.append(2)
                elif char == 'd':
                    arr.append(3)
                elif char == 'e':
                    arr.append(4)
                elif char == 'f':
                    arr.append(5)
                elif char == 'g':
                    arr.append(6)
                elif char == 'h':
                    arr.append(7)
                
            print("Where would you like this piece to go?")
            input_end_cords = input()
            arr2 = []
            for char in input_end_cords:
                if char == '1':
                    arr2.append(7)
                elif char == '2':
                    arr2.append(6)
                elif char == '3':
                    arr2.append(5)
                elif char == '4':
                    arr2.append(4)
                elif char == '5':
                    arr2.append(3)
                elif char == '6':
                    arr2.append(2)
                elif char == '7':
                    arr2.append(1)
                elif char == '8':
                    arr2.append(0)
                elif char == 'a':
                    arr2.append(0)
                elif char == 'b':
                    arr2.append(1)
                elif char == 'c':
                    arr2.append(2)
                elif char == 'd':
                    arr2.append(3)
                elif char == 'e':
                    arr2.append(4)
                elif char == 'f':
                    arr2.append(5)
                elif char == 'g':
                    arr2.append(6)
                elif char == 'h':
                    arr2.append(7)

                
            swap_positions(arr, arr2)

CLI()