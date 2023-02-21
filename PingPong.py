import pygame as pg
import random

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((1000, 750))
        self.screen.fill((0,0,0))
        self.p1_x = 10
        self.p1_y = 325
        self.p2_x = 960
        self.p2_y = 325
        self.p_width = 30
        self.p_height = 150
        self.p1_point = 0
        self.p2_point = 0
        self.b_x = 500
        self.b_y = 375
        self.bx = random.randint(-15,15)
        self.by = random.randint(-6,6)
        if self.bx == 0:
            self.bx = 5
        elif self.by == 0:
            self.by = 3
        
    def bmove(self):
        self.b_x += self.bx
        self.b_y += self.by

    def collide_with_wall(self):
        '''if self.b_x+20 >= 1000 or self.b_x-20 <= 0:
            self.bx *= -1'''
        if self.b_y+20 >= 750 or self.b_y-20 <=0:
            self.by *= -1

    
    def randball(self):
        self.b_x = 500
        self.bx = random.randint(-15,15)
        self.by = random.randint(-6,6)
    
    def score(self):
        font = pg.font.SysFont('arial', 50)
        sc1 = font.render(self.p1_point, True, (255,255,255))
        self.screen.blit(sc1, ())
        sc2 = font.render(self.p2_point, True, (255,255,255))
    
    def lose(self):
        if self.b_x>=1000:
            self.p2_point += 1
            self.randball()
        
        elif self.b_x<=0:
            self.p1_point += 1
            self.randball()
    
    def cheat(self):
        self.bx *= -1

    def inc_speed(self):
        if self.b_x > 500:
            self.bx+=5
        if self.b_x<500:
            self.bx-=5
    
    def dec_speed(self):
        if self.b_x>500:
            self.bx-=5
        if self.b_x<500:
            self.bx+=5

        
    def is_collide(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.pl1 = pg.math.Vector2(self.p1_x+self.p_width, self.p1_y)
        self.pl2 = pg.math.Vector2(self.p2_x-self.p_width, self.p2_y)
        self.bp1 = pg.math.Vector2(self.b_x-20, self.b_y)
        self.bp2 = pg.math.Vector2(self.b_x+20, self.b_y)

        if self.p1.collidepoint(self.bp1):
            self.bx *= -1
        
        if self.p2.collidepoint(self.bp2):
            self.bx *= -1


    def run(self):
        work = True

        while work:
            pg.time.delay(50)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    work = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        self.p1_y -= 20
                    elif event.key == pg.K_s:
                        self.p1_y += 20

                    elif event.key == pg.K_UP:
                        self.p2_y -= 20
                    elif event.key == pg.K_DOWN:
                        self.p2_y += 20
                    elif event.key == pg.K_r:
                        self.randball()
                    elif event.key == pg.K_LCTRL:
                        self.cheat()
                    elif event.key == pg.K_8:
                        self.inc_speed()
                    elif event.key == pg.K_2:
                        self.dec_speed()
    
            self.screen.fill((0,0,0))
            p1 = pg.draw.rect(self.screen, (255,255,255), pg.Rect(self.p1_x,self.p1_y,self.p_width,self.p_height))
            p2 = pg.draw.rect(self.screen, (255,255,255), pg.Rect(self.p2_x,self.p2_y, self.p_width,self.p_height))
            b = ball(self.screen, self.b_x, self.b_y)
            pg.draw.line(self.screen, (255,255,255), (500,0), (500,750), 2)
            self.bmove()
            self.is_collide(p1, p2)
            self.collide_with_wall()
            self.lose()
            pg.display.update()


class ball():
    def __init__(self, screen, x, y):
        self.b_x = x
        self.b_y = y
        self.screen = screen
        pg.draw.circle(self.screen, (255,255,255), (self.b_x, self.b_y), 20)


g1 = Game()
g1.run()
