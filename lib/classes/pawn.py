class Pawn:

    def __init__(self, pos):
        self.pos = pos
        self.n_pos = [pos[0] - 1, pos[1]] # it goes to -1, prevent this
        self.nw_pos = [pos[0] - 1, pos[1] - 1]
        self.ne_pos = [pos[0] - 1, pos[1] + 1]

    def __repr__(self):
        return "♟"