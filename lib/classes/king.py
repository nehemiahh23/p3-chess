class King:

    # give the king its own movement function to prevent putting self in check
    def __init__(self, pos):
        self.pos = pos
        self.n_pos = [pos[0] - 1, pos[1]]
        self.ne_pos = [pos[0] - 1, pos[1] + 1]
        self.e_pos = [pos[0], pos[1] + 1]
        self.se_pos = [pos[0] + 1, pos[1] + 1]
        self.s_pos = [pos[0] + 1, pos[1]]
        self.sw_pos = [pos[0] + 1, pos[1] - 1]
        self.w_pos = [pos[0], pos[1] - 1]
        self.nw_pos = [pos[0] - 1, pos[1] - 1]

    def __repr__(self):
        return "♚"