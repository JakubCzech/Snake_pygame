import file_body_element

class _Snake:
    body = []
    direction = 0
    color = (0, 107, 11)
    x_change = 0
    y_change = 0
    def __init__(self,windows_width,window_height):
        self.start_head_pos_x = windows_width/2
        self.start_head_pos_y = window_height/2
        self.head = file_body_element._Body_Element(self.start_head_pos_x, self.start_head_pos_y,(0, 36, 4))
        self.body.append(self.head)
        self.size = 10

    def longer(self):
        tmp = file_body_element._Body_Element(0, 0)
        self.body.append(tmp)

    def change_direction(self, new_direction):
        if new_direction == 1 and  self.y_change!=-self.size :
            self.y_change=self.size
            self.x_change=0
        if new_direction == 2 and self.y_change != self.size:
            self.y_change = -self.size
            self.x_change = 0

        if new_direction == 3 and self.x_change != -self.size:
            self.x_change = self.size
            self.y_change = 0

        if new_direction == 4 and self.x_change != self.size:
            self.x_change = -self.size
            self.y_change = 0

    def __del__(self):
        del self
    def move(self):
        for i in range(len(self.body)-1,0,-1):
            if (i>0):
                self.body[i].set_pos_x(self.body[i - 1].get_pos_x())
                self.body[i].set_pos_y(self.body[i - 1].get_pos_y())
        self.body[0].set_pos_y(self.body[0].get_pos_y() + self.y_change)
        self.body[0].set_pos_x(self.body[0].get_pos_x() + self.x_change)


