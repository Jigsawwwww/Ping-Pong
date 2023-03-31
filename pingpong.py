from pygame import *
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_name,speed,x,y):
        super().__init__()
        self.image=transform.scale(image.load(player_name),(30,100))
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


window = display.set_mode((700,500))
display.set_caption('Ping-Pong')
fps=120
clock=time.Clock()
game=True
finish=False         
while game:
    display.update()
    clock.tick(fps)      
