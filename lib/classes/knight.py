class Knight:

    # RENAME PAWN MOVES
    def __init__(self, pos):
        self.pos = pos
        self.ne_pos = [pos[0] - 2, pos[1] + 1]
        self.se_pos = [pos[0] + 2, pos[1] + 1]
        self.sw_pos = [pos[0] + 2, pos[1] - 1]
        self.nw_pos = [pos[0] - 2, pos[1] - 1]

    def __repr__(self):
        return "♞"