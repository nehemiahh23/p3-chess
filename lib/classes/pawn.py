class Pawn:

    def __init__(self, pos):
        self.pos = pos
        self.move_forward = [pos[0] + 1, pos[1]]
        self.move_diag_r = [pos[0] + 1, pos[1] + 1]
        self.move_diag_l = [pos[0] + 1, pos[1] - 1]
