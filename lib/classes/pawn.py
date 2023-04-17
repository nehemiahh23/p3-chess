class Pawn:

    def __init__(self, pos, black=False):
        self.pos = pos
        self.black = black
        self.n_pos = [pos[0] - 1, pos[1]] # it goes to -1, prevent this
        self.nw_pos = [pos[0] - 1, pos[1] - 1]
        self.ne_pos = [pos[0] - 1, pos[1] + 1]

    def __repr__(self):
        if self.black:
            return "♙"
        else:
            return "♟"