class Pawn:

    def __init__(self, pos, black=False):
        self.pos = pos
        self.black = black
        self.calc()

    def calc(self):
        self.n_pos = [self.pos[0] - 1, self.pos[1]]
        self.nw_pos = [self.pos[0] - 1, self.pos[1] - 1]
        self.ne_pos = [self.pos[0] - 1, self.pos[1] + 1]

    def __repr__(self):
        if self.black:
            return "♙"
        else:
            return "♟"