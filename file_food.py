class _Food:
    color = (107, 0, 0)
    def __init__(self, pos_x, pos_y, live = 100):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.live = live
    def get_pos_x(self):
        return self.pos_x
    def get_pos_y(self):
        return self.pos_y
    def live_decrement(self):
        self.live -=1