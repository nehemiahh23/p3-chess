class Rook:

    def __init__(self, pos):
        self.pos = pos
        self.n1_pos = [pos[0] - 1, pos[1]]
        self.n2_pos = [pos[0] - 2, pos[1]]
        self.n3_pos = [pos[0] - 3, pos[1]]
        self.n4_pos = [pos[0] - 4, pos[1]]
        self.n5_pos = [pos[0] - 5, pos[1]]
        self.n6_pos = [pos[0] - 6, pos[1]]
        self.n7_pos = [pos[0] - 7, pos[1]]
        self.n8_pos = [pos[0] - 8, pos[1]]
        
        self.e1_pos = [pos[0], pos[1] + 1]
        self.e2_pos = [pos[0], pos[1] + 2]
        self.e3_pos = [pos[0], pos[1] + 3]
        self.e4_pos = [pos[0], pos[1] + 4]
        self.e5_pos = [pos[0], pos[1] + 5]
        self.e6_pos = [pos[0], pos[1] + 6]
        self.e7_pos = [pos[0], pos[1] + 7]
        self.e8_pos = [pos[0], pos[1] + 8]

        self.s1_pos = [pos[0] + 1, pos[1]]
        self.s2_pos = [pos[0] + 2, pos[1]]
        self.s3_pos = [pos[0] + 3, pos[1]]
        self.s4_pos = [pos[0] + 4, pos[1]]
        self.s5_pos = [pos[0] + 5, pos[1]]
        self.s6_pos = [pos[0] + 6, pos[1]]
        self.s7_pos = [pos[0] + 7, pos[1]]
        self.s8_pos = [pos[0] + 8, pos[1]]
        
        self.w1_pos = [pos[0], pos[1] - 1]
        self.w2_pos = [pos[0], pos[1] - 2]
        self.w3_pos = [pos[0], pos[1] - 3]
        self.w4_pos = [pos[0], pos[1] - 4]
        self.w5_pos = [pos[0], pos[1] - 5]
        self.w6_pos = [pos[0], pos[1] - 6]
        self.w7_pos = [pos[0], pos[1] - 7]
        self.w8_pos = [pos[0], pos[1] - 8]

    def __repr__(self):
        return "♜"