class Bishop:

    def __init__(self, pos, black=False):
        self.pos = pos
        self.black = black
        self.cptd = False
        self.calc()
        self.positions = [[self.ne1_pos, self.ne2_pos, self.ne3_pos, self.ne4_pos, self.ne5_pos, self.ne6_pos, self.ne7_pos], [self.se1_pos, self.se2_pos, self.se3_pos, self.se4_pos, self.se5_pos, self.se6_pos, self.se7_pos], [self.sw1_pos, self.sw2_pos, self.sw3_pos, self.sw4_pos, self.sw5_pos, self.sw6_pos, self.sw7_pos], [self.nw1_pos, self.nw2_pos, self.nw3_pos, self.nw4_pos, self.nw5_pos, self.nw6_pos, self.nw7_pos]]

    def calc(self):
        self.ne1_pos = [self.pos[0] - 1, self.pos[1] + 1]
        self.ne2_pos = [self.pos[0] - 2, self.pos[1] + 2]
        self.ne3_pos = [self.pos[0] - 3, self.pos[1] + 3]
        self.ne4_pos = [self.pos[0] - 4, self.pos[1] + 4]
        self.ne5_pos = [self.pos[0] - 5, self.pos[1] + 5]
        self.ne6_pos = [self.pos[0] - 6, self.pos[1] + 6]
        self.ne7_pos = [self.pos[0] - 7, self.pos[1] + 7]

        self.se1_pos = [self.pos[0] + 1, self.pos[1] + 1]
        self.se2_pos = [self.pos[0] + 2, self.pos[1] + 2]
        self.se3_pos = [self.pos[0] + 3, self.pos[1] + 3]
        self.se4_pos = [self.pos[0] + 4, self.pos[1] + 4]
        self.se5_pos = [self.pos[0] + 5, self.pos[1] + 5]
        self.se6_pos = [self.pos[0] + 6, self.pos[1] + 6]
        self.se7_pos = [self.pos[0] + 7, self.pos[1] + 7]

        self.sw1_pos = [self.pos[0] + 1, self.pos[1] - 1]
        self.sw2_pos = [self.pos[0] + 2, self.pos[1] - 2]
        self.sw3_pos = [self.pos[0] + 3, self.pos[1] - 3]
        self.sw4_pos = [self.pos[0] + 4, self.pos[1] - 4]
        self.sw5_pos = [self.pos[0] + 5, self.pos[1] - 5]
        self.sw6_pos = [self.pos[0] + 6, self.pos[1] - 6]
        self.sw7_pos = [self.pos[0] + 7, self.pos[1] - 7]

        self.nw1_pos = [self.pos[0] - 1, self.pos[1] - 1]
        self.nw2_pos = [self.pos[0] - 2, self.pos[1] - 2]
        self.nw3_pos = [self.pos[0] - 3, self.pos[1] - 3]
        self.nw4_pos = [self.pos[0] - 4, self.pos[1] - 4]
        self.nw5_pos = [self.pos[0] - 5, self.pos[1] - 5]
        self.nw6_pos = [self.pos[0] - 6, self.pos[1] - 6]
        self.nw7_pos = [self.pos[0] - 7, self.pos[1] - 7]

    def __repr__(self):
        if self.cptd:
            return "□"
        else:
            if self.black:
                return "♗"
            else:
                return "♝"