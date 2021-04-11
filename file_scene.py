import file_snake
import file_food

import pygame
import random
class _Scene:
    score = 0
    game_over = 0
    tick = 5
    color = (172, 189, 176)
    color_font =(255, 255, 102)
    border_color = (1, 0, 36)
    def __init__(self,dis_width=600,dis_height=400,title='Snake',border = 0):
        self.width = dis_width
        self.height = dis_height
        self.title = title
        self.border = border
        self.snake = file_snake._Snake(self.width,self.height)
        pygame.init()

        self.display = pygame.display.set_mode((self.width,  self.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.font_style = pygame.font.SysFont("bahnschrift", 20)
        self.score_font = pygame.font.SysFont("comicsansms", 35)


    def draw(self):
        self.display.fill(self.color)
        if (self.border):
            pygame.draw.rect(self.display, self.border_color ,(0, 0, self.width, self.snake.size))
            pygame.draw.rect(self.display, self.border_color, (0, 0, self.snake.size, self.height))
            pygame.draw.rect(self.display, self.border_color, (self.height-self.snake.size,0, self.width,self.height))
            pygame.draw.rect(self.display, self.border_color, (0,self.width-self.snake.size, self.width,self.height))
        value = self.score_font.render("Wynik: " + str(self.score), True, self.color_font)
        self.display.blit(value, [0, 0])
        for x in self.snake.body:
            pygame.draw.rect(self.display,x.color,[x.pos_x,x.pos_y,self.snake.size,self.snake.size])

        pygame.draw.rect(self.display, self.food.color,[self.food.get_pos_x(), self.food.get_pos_y(), self.snake.size, self.snake.size])
        pygame.display.update()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = 1
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.change_direction(4)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(3)
                elif event.key == pygame.K_UP:
                    self.snake.change_direction(2)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(1)

    def game_loop(self):
        self.food = file_food._Food(random.randrange(0, self.width, 10), random.randrange(0, self.height, 10))
        self.draw()
        while not self.game_over:
            self.update()
            self.checkPosition()
            self.snake.move()
            self.draw()
            if(self.food.live == 0):
                self.food = 0
                if(self.border):
                    self.food = file_food._Food(random.randrange(0 + self.snake.size, self.width - self.snake.size, 10),random.randrange(0 + self.snake.size, self.height - self.snake.size, 10))
                else:
                    self.food = file_food._Food(random.randrange(0, self.width, 10), random.randrange(0, self.height, 10))

            else:
                self.food.live_decrement()

            self.clock.tick(self.tick)
        self.quit()
    def score_up(self):
        self.score += 1
        self.food.live = 0
        self.snake.longer()
        self.tick +=0.5

    def checkPosition(self):
        if (self.border):
            if self.snake.body[0].get_pos_x() <= 0+self.snake.size:
                self.game_over = True
            if self.snake.body[0].get_pos_y() <= 0+self.snake.size:
                self.game_over = True
            if self.snake.body[0].get_pos_x() >= self.width - self.snake.size:
                self.game_over = True
            if self.snake.body[0].get_pos_y() >= self.height - self.snake.size:
                self.game_over = True
        else:
            if self.snake.body[0].get_pos_x()< 0:
                self.snake.body[0].set_pos_x(self.width-self.snake.size)
            if self.snake.body[0].get_pos_y()< 0:
                self.snake.body[0].set_pos_y(self.height - self.snake.size)
            if self.snake.body[0].get_pos_x()>= self.width:
                self.snake.body[0].set_pos_x(0)
            if self.snake.body[0].get_pos_y() >= self.height:
                self.snake.body[0].set_pos_y(0)
        if self.snake.body[0].get_pos_x() == self.food.get_pos_x() and self.snake.body[0].get_pos_y() == self.food.get_pos_y():
            self.score_up()

        tmp_head_pos = (self.snake.body[0].get_pos_x(),self.snake.body[0].get_pos_y())
        for x in range(len(self.snake.body)):
            if x != 0:
                if self.snake.body[x].get_pos_x() == tmp_head_pos[0] and self.snake.body[x].get_pos_y() == tmp_head_pos[1]:
                    self.game_over=True

    def quit(self):

        new_game = 99
        while new_game==99:
            self.display.fill(self.color)
            value = self.score_font.render("Wynik: " + str(self.score), True, self.color_font)
            self.display.blit(value, [self.width/2, self.height/2])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        new_game = 0
        pygame.quit()
