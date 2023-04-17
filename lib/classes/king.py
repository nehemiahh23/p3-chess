class King:

    # give the king its own movement function to prevent putting self in check
    def __init__(self, pos, black=False):
        self.pos = pos
        self.black = black
        self.cptd = False
        self.calc()

    def calc(self):
        self.n_pos = [self.pos[0] - 1, self.pos[1]]
        self.ne_pos = [self.pos[0] - 1, self.pos[1] + 1]
        self.e_pos = [self.pos[0], self.pos[1] + 1]
        self.se_pos = [self.pos[0] + 1, self.pos[1] + 1]
        self.s_pos = [self.pos[0] + 1, self.pos[1]]
        self.sw_pos = [self.pos[0] + 1, self.pos[1] - 1]
        self.w_pos = [self.pos[0], self.pos[1] - 1]
        self.nw_pos = [self.pos[0] - 1, self.pos[1] - 1]

    def __repr__(self):
        if self.cptd:
            return "□"
        else:
            if self.black:
                return "♔"
            else:
                return "♚"