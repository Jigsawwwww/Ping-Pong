from pygame import *
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_name,speed,x,y, sx, sy):
        super().__init__()
        self.image=transform.scale(image.load(player_name),(sx,sy))
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w] and self.rect.y<450:
            self.rect.y-=self.speed
        elif keys_pressed[K_s] and self.rect.y>50:
            self.rect.y+=self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y<450:
            self.rect.y-=self.speed
        elif keys_pressed[K_DOWN] and self.rect.y>50:
            self.rect.y+=self.speed

class Ball(GameSprite):
    def __init__(self,image,speedx,speedy,x,y,sizex,sizey):
        super().__init__(image, speedx, x, y, sizex, sizey)
        self.speed2=speedy
    def update(self,r1,r2):
        self.rect.x+=self.speed
        self.rect.y+=self.speed2
        if sprite.collide_rect(self,r1):
            self.speed*=-1
        if sprite.collide_rect(self,r2):
            self.speed*=-1
        if self.rect.y<=0:
            self.speed2*=-1
        if self.rect.y>=500:
            self.speed2*=-1

window = display.set_mode((700,500))
display.set_caption('Ping-Pong')
window.fill((150,150,150))
fps=60
font.init()
font1 = font.SysFont('Arial', 19)
clock=time.Clock()
player1 = Player1("a.png",10,50,70, 30, 100)
player2 = Player2("a.png",10,600,70, 30, 100)
ball = Ball('ball2.png',5,5,350,250,35,35)
game=True
finish=False         
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish!=True:
        window.fill((150,150,150))
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.reset()
        ball.update(player1, player2)
        if ball.rect.x>=690 or ball.rect.x<=10:        
            finish=True
    text2 = font1.render('Вы проиграли',1,(255,255,255))
    display.update()
    clock.tick(fps)      
