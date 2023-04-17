class Pawn:

    def __init__(self, pos):
        self.pos = pos
        self.forward_pos = [pos[0] - 1, pos[1]] # it goes to -1, prevent this
        self.diag_l_pos = [pos[0] - 1, pos[1] - 1]
        self.diag_r_pos = [pos[0] - 1, pos[1] + 1]

    def __repr__(self):
        return "♟"