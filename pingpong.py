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
window.fill((102,102,255))
fps=120
clock=time.Clock()
player1 = Player1("a.png",10,50,70)
player2 = Player2("a.png",10,600,70)
game=True
finish=False         
while game:
    player1.reset()
    player1.update()
    player2.reset()
    player2.update()
    display.update()
    clock.tick(fps)      
