import pygame as pg
import random

size = 40

class apple:
    def __init__(self, parent_screen):
        self.apple = pg.image.load("apple.png").convert()
        self.apple = pg.transform.scale(self.apple, (40,40))
        self.parent_screen = parent_screen
        self.apple_x = size * 3
        self.apple_y = size * 3

    def draw(self):
        self.parent_screen.blit(self.apple, (self.apple_x, self.apple_y))
        pg.display.update()

    def move(self):
        self.apple_x = random.randint(0,20) * size
        self.apple_y = random.randint(0,15) * size


class snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.snake = pg.image.load("g blck.png").convert()
        self.snake = pg.transform.scale(self.snake, (40,40))
        self.snake_x = [size]*length
        self.snake_y = [size]*length
        self.direction = ""

    def inc_len(self):
        self.length += 1
        self.snake_x.append(-1)
        self.snake_y.append(-1)

        
    def draw(self):
        self.parent_screen.fill((255,255,0))
        for i in range(self.length):
            self.parent_screen.blit(self.snake, (self.snake_x[i], self.snake_y[i]))
        pg.display.update()

    
    def walk(self):

        for i in range(self.length-1, 0, -1):
            self.snake_x[i] = self.snake_x[i-1]
            self.snake_y[i] = self.snake_y[i-1]

        if self.direction == "up":
            self.snake_y[0] -= size
        
        if self.direction == "down":
            self.snake_y[0] += size

        if self.direction == "left":
            self.snake_x[0] -= size
        
        if self.direction == "right":
            self.snake_x[0] += size

        self.draw()


    def move_left(self):
        
        self.direction = "left"
    
    def move_right(self):
        
        self.direction = "right"

    def move_up(self):
        
        self.direction = "up"
        
    def move_down(self):
        
        self.direction = "down"


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1000, 760))
        self.screen.fill((255,255,0))
        self.snake = snake(self.screen, 1)
        self.snake.draw()
        self.apple = apple(self.screen)
        self.apple.draw()
        

    
    def is_collision(self, x1, y1, x2, y2):
        '''if x1 >= x2 and x1<x2*size:
            if y1>= y2 and y1 < y2*size:
                return True'''

        if x1 == x2 and y1 == y2:
            return True

        return False


    def play(self):
        self.snake.walk()
        self.apple.draw()

    def display_score(self):
        font = pg.font.SysFont('arial', 30)
        score =  font.render(f"Score : {self.snake.length}", True, (0,0,0))
        self.screen.blit(score, (800,10))

    def game_over(self):
        self.screen.fill((255,255,0))
        font = pg.font.SysFont('arial', 30)
        l1 = font.render(f"Game Over! Your score is {self.snake.length}", True, (0,0,0))
        self.screen.blit(l1, (200,300))
        l2 = font.render(f"To play again press Enter", True, (0,0,0))
        self.screen.blit(l2, (300,400))
        pg.display.update()

    def run(self):

        runn = True
        pause = False

        while runn:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        runn = False

                    if not pause:                    
                        if event.key == pg.K_w:
                            self.snake.move_up()
                            self.snake.walk()

                        if event.key == pg.K_s:
                            self.snake.move_down()
                            self.snake.walk()
                        
                        if event.key == pg.K_a:
                            self.snake.move_left()
                            self.snake.walk()

                        
                        if event.key == pg.K_d:
                            self.snake.move_right()
                            self.snake.walk()

                    elif event.type == pg.QUIT:
                        runn = False
                    
                    elif event.key == pg.K_RETURN:
                        pause = True
                    
                    

            if not pause:

                self.display_score()
                if self.is_collision(self.snake.snake_x[0], self.snake.snake_y[0], self.apple.apple_x, self.apple.apple_y):
                    self.snake.inc_len()
                    self.apple.move()
                try:
                    for i in range(3,self.snake.length):
                        if self.is_collision(self.snake.snake_x[0], self.snake.snake_y[0], self.snake.snake_x[i], self.snake.snake_y[i]):
                            raise Exception
                except Exception:
                    self.game_over()
                self.apple.draw()
            


game = Game()
game.run()