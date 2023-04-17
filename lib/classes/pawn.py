class Pawn:

    def __init__(self, pos, black=False):
        self.pos = pos
        self._start = pos
        self.black = black
        self.calc()

    def calc(self):
        if self.black == False:
            if self.pos == self._start:
                self.n2_pos = [self.pos[0] - 2, self.pos[1]]
            self.n_pos = [self.pos[0] - 1, self.pos[1]]
            self.nw_pos = [self.pos[0] - 1, self.pos[1] - 1]
            self.ne_pos = [self.pos[0] - 1, self.pos[1] + 1]
        else:
            if self.pos == self._start:
                self.s2_pos = [self.pos[0] + 2, self.pos[1]]
            self.s_pos = [self.pos[0] + 1, self.pos[1]]
            self.sw_pos = [self.pos[0] + 1, self.pos[1] - 1]
            self.se_pos = [self.pos[0] + 1, self.pos[1] + 1]

    def __repr__(self):
        if self.black:
            return "♙"
        else:
            return "♟"