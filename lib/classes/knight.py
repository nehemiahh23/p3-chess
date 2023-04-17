class Knight:

    # RENAME PAWN MOVES
    def __init__(self, pos, black=False):
        self.pos = pos
        self.black = black
        self.ne_pos = []
        self.se_pos = []
        self.sw_pos = []
        self.nw_pos = []
        self.calc()

    def calc(self):
        self.nne_pos = [self.pos[0] - 2, self.pos[1] + 1]
        self.nee_pos = [self.pos[0] - 1, self.pos[1] + 2]
        self.sse_pos = [self.pos[0] + 2, self.pos[1] + 1]
        self.see_pos = [self.pos[0] + 1, self.pos[1] + 2]
        self.ssw_pos = [self.pos[0] + 2, self.pos[1] - 1]
        self.sww_pos = [self.pos[0] + 1, self.pos[1] - 2]
        self.nnw_pos = [self.pos[0] - 2, self.pos[1] - 1]
        self.nww_pos = [self.pos[0] - 1, self.pos[1] - 2]

    def __repr__(self):
        if self.black:
            return "♘"
        else:
            return "♞"