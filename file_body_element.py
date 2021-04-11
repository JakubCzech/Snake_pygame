class _Body_Element:
    def __init__(self, pos_x, pos_y,color_tmp =(0, 107, 11)):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color_tmp
    def get_pos_x(self):
        return self.pos_x
    def get_pos_y(self):
        return self.pos_y
    def set_pos_x(self, p_x):
        self.pos_x = p_x
    def set_pos_y(self, p_y):
        self.pos_y = p_y