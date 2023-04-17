class Rook:

    def __init__(self, pos, black=False):
        self.pos = pos
        self.black = black
        self.calc()

    def calc(self):
        self.n1_pos = [self.pos[0] - 1, self.pos[1]]
        self.n2_pos = [self.pos[0] - 2, self.pos[1]]
        self.n3_pos = [self.pos[0] - 3, self.pos[1]]
        self.n4_pos = [self.pos[0] - 4, self.pos[1]]
        self.n5_pos = [self.pos[0] - 5, self.pos[1]]
        self.n6_pos = [self.pos[0] - 6, self.pos[1]]
        self.n7_pos = [self.pos[0] - 7, self.pos[1]]
        self.n8_pos = [self.pos[0] - 8, self.pos[1]]
        
        self.e1_pos = [self.pos[0], self.pos[1] + 1]
        self.e2_pos = [self.pos[0], self.pos[1] + 2]
        self.e3_pos = [self.pos[0], self.pos[1] + 3]
        self.e4_pos = [self.pos[0], self.pos[1] + 4]
        self.e5_pos = [self.pos[0], self.pos[1] + 5]
        self.e6_pos = [self.pos[0], self.pos[1] + 6]
        self.e7_pos = [self.pos[0], self.pos[1] + 7]
        self.e8_pos = [self.pos[0], self.pos[1] + 8]

        self.s1_pos = [self.pos[0] + 1, self.pos[1]]
        self.s2_pos = [self.pos[0] + 2, self.pos[1]]
        self.s3_pos = [self.pos[0] + 3, self.pos[1]]
        self.s4_pos = [self.pos[0] + 4, self.pos[1]]
        self.s5_pos = [self.pos[0] + 5, self.pos[1]]
        self.s6_pos = [self.pos[0] + 6, self.pos[1]]
        self.s7_pos = [self.pos[0] + 7, self.pos[1]]
        self.s8_pos = [self.pos[0] + 8, self.pos[1]]
        
        self.w1_pos = [self.pos[0], self.pos[1] - 1]
        self.w2_pos = [self.pos[0], self.pos[1] - 2]
        self.w3_pos = [self.pos[0], self.pos[1] - 3]
        self.w4_pos = [self.pos[0], self.pos[1] - 4]
        self.w5_pos = [self.pos[0], self.pos[1] - 5]
        self.w6_pos = [self.pos[0], self.pos[1] - 6]
        self.w7_pos = [self.pos[0], self.pos[1] - 7]
        self.w8_pos = [self.pos[0], self.pos[1] - 8]

    def __repr__(self):
        if self.black:
            return "♖"
        else:
            return "♜"