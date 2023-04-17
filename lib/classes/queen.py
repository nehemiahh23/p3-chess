class Queen:

    def __init__(self, pos, black=False):
        self.pos = pos
        self.black = black

        self.n1_pos = [pos[0] - 1, pos[1]]
        self.n2_pos = [pos[0] - 2, pos[1]]
        self.n3_pos = [pos[0] - 3, pos[1]]
        self.n4_pos = [pos[0] - 4, pos[1]]
        self.n5_pos = [pos[0] - 5, pos[1]]
        self.n6_pos = [pos[0] - 6, pos[1]]
        self.n7_pos = [pos[0] - 7, pos[1]]
        self.n8_pos = [pos[0] - 8, pos[1]]

        self.ne1_pos = [pos[0] - 1, pos[1] + 1]
        self.ne2_pos = [pos[0] - 2, pos[1] + 2]
        self.ne3_pos = [pos[0] - 3, pos[1] + 3]
        self.ne4_pos = [pos[0] - 4, pos[1] + 4]
        self.ne5_pos = [pos[0] - 5, pos[1] + 5]
        self.ne6_pos = [pos[0] - 6, pos[1] + 6]
        self.ne7_pos = [pos[0] - 7, pos[1] + 7]
        self.ne8_pos = [pos[0] - 8, pos[1] + 8]

        self.e1_pos = [pos[0], pos[1] + 1]
        self.e2_pos = [pos[0], pos[1] + 2]
        self.e3_pos = [pos[0], pos[1] + 3]
        self.e4_pos = [pos[0], pos[1] + 4]
        self.e5_pos = [pos[0], pos[1] + 5]
        self.e6_pos = [pos[0], pos[1] + 6]
        self.e7_pos = [pos[0], pos[1] + 7]
        self.e8_pos = [pos[0], pos[1] + 8]

        self.se1_pos = [pos[0] + 1, pos[1] + 1]
        self.se2_pos = [pos[0] + 2, pos[1] + 2]
        self.se3_pos = [pos[0] + 3, pos[1] + 3]
        self.se4_pos = [pos[0] + 4, pos[1] + 4]
        self.se5_pos = [pos[0] + 5, pos[1] + 5]
        self.se6_pos = [pos[0] + 6, pos[1] + 6]
        self.se7_pos = [pos[0] + 7, pos[1] + 7]
        self.se8_pos = [pos[0] + 8, pos[1] + 8]

        self.s1_pos = [pos[0] + 1, pos[1]]
        self.s2_pos = [pos[0] + 2, pos[1]]
        self.s3_pos = [pos[0] + 3, pos[1]]
        self.s4_pos = [pos[0] + 4, pos[1]]
        self.s5_pos = [pos[0] + 5, pos[1]]
        self.s6_pos = [pos[0] + 6, pos[1]]
        self.s7_pos = [pos[0] + 7, pos[1]]
        self.s8_pos = [pos[0] + 8, pos[1]]

        self.sw1_pos = [pos[0] + 1, pos[1] - 1]
        self.sw2_pos = [pos[0] + 2, pos[1] - 2]
        self.sw3_pos = [pos[0] + 3, pos[1] - 3]
        self.sw4_pos = [pos[0] + 4, pos[1] - 4]
        self.sw5_pos = [pos[0] + 5, pos[1] - 5]
        self.sw6_pos = [pos[0] + 6, pos[1] - 6]
        self.sw7_pos = [pos[0] + 7, pos[1] - 7]
        self.sw8_pos = [pos[0] + 8, pos[1] - 8]

        self.w1_pos = [pos[0], pos[1] - 1]
        self.w2_pos = [pos[0], pos[1] - 2]
        self.w3_pos = [pos[0], pos[1] - 3]
        self.w4_pos = [pos[0], pos[1] - 4]
        self.w5_pos = [pos[0], pos[1] - 5]
        self.w6_pos = [pos[0], pos[1] - 6]
        self.w7_pos = [pos[0], pos[1] - 7]
        self.w8_pos = [pos[0], pos[1] - 8]

        self.nw1_pos = [pos[0] - 1, pos[1] - 1]
        self.nw2_pos = [pos[0] - 2, pos[1] - 2]
        self.nw3_pos = [pos[0] - 3, pos[1] - 3]
        self.nw4_pos = [pos[0] - 4, pos[1] - 4]
        self.nw5_pos = [pos[0] - 5, pos[1] - 5]
        self.nw6_pos = [pos[0] - 6, pos[1] - 6]
        self.nw7_pos = [pos[0] - 7, pos[1] - 7]
        self.nw8_pos = [pos[0] - 8, pos[1] - 8]

    def __repr__(self):
        if self.black:
            return "♕"
        else:
            return "♛"