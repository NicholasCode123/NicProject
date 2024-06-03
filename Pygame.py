import pygame as py
from sys import exit
from random import randint,choice

class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=py.Surface((30,30))
        self.image.fill('white')
        self.gravity=0
        self.rect = self.image.get_rect(midbottom=(200,600))
    def movement(self):
        self.gravity+=0.35
        self.rect.y+=self.gravity   
        keys=py.key.get_pressed()
        if keys[py.K_LEFT] or keys[py.K_a]:
            self.rect.x-=2
        elif keys[py.K_RIGHT] or keys[py.K_d]:
            self.rect.x+=2
        if keys[py.K_UP] or keys[py.K_w]:
            if self.rect.bottom >=600:
                self.gravity=0
                self.gravity-=12
                self.rect.y+=self.gravity
        if self.rect.right <= 0:
            self.rect.right=420
        elif self.rect.left >= 400:
            self.rect.left=-20
        if self.rect.bottom > 600:
            self.rect.bottom=600
        
        
            
    def update(self):
        self.movement()
        if game == False:
            self.rect.bottom=600
            self.rect.x=200
class Obstacle(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.random=randint(20,70)
        self.gravity=0
        self.image=py.Surface((self.random,self.random))
        self.image.fill('red')
        self.rect = self.image.get_rect(midbottom=(randint(0,400),0))
    def falling(self):
        self.gravity+=0.02
        self.rect.y+=self.gravity
    def update(self):
        self.falling()
        self.obstacle_out_of_area()
    def obstacle_out_of_area(self):
        if self.rect.y >= 700:
            self.kill()

class Obstacle2(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.random=randint(10,40)
        self.image=py.Surface((self.random,self.random))
        self.image.fill('blue')
        self.spawn=choice([randint(-50,-10),randint(410,450)])
        self.rect = self.image.get_rect(midbottom=(choice([randint(-50,-10),randint(410,450)]),600))
    def movement(self):
        if self.spawn < 0:
            self.rect.x+=2
        else:
            self.rect.x-=2
    def update(self):
        self.movement()
        self.obstacle_out_of_area()
    def obstacle_out_of_area(self):
        if self.rect.x >= 450 or self.rect.x <= -50:
            self.kill()
def score():
    skor=round((py.time.get_ticks()-hitungan_skor)/1000,1)
    font_game=py.font.Font('font/Pixeltype.ttf',50)
    font_render=font_game.render(f'Score:{skor}',True,'White')
    font_rec=font_render.get_rect(center=(200,300))
    surface.blit(font_render,font_rec)
    return skor


py.init()
fps=py.time.Clock()
surface=py.display.set_mode((400,600))
font_game=py.font.Font('font/Pixeltype.ttf',50)
font_render=font_game.render("Press space to start",True,'White')
font_rec=font_render.get_rect(center=(200,300))
player=py.sprite.GroupSingle()
player.add(Player())
obstacle=py.sprite.Group()
obstacle2=py.sprite.Group()
obstacle_timer=py.USEREVENT+1
py.time.set_timer(obstacle_timer,400)
obstacle_timer2=py.USEREVENT+2
py.time.set_timer(obstacle_timer2,1000)
game=False
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        if game:
            if event.type == obstacle_timer:
                obstacle.add(Obstacle())
            if event.type == obstacle_timer2:
                obstacle2.add(Obstacle2())
    if game:
        surface.fill('black')
        player.draw(surface)
        player.update()
        obstacle.draw(surface)
        obstacle.update()
        obstacle2.draw(surface)
        obstacle2.update()
        score()
        collide=py.sprite.spritecollide(player.sprite,obstacle,False) 
        collide2=py.sprite.spritecollide(player.sprite,obstacle2,False) 
        if collide or collide2 :
            game=False
        fps.tick(180)
    else:
        hitungan_skor=py.time.get_ticks()
        obstacle.empty()
        obstacle2.empty()
        player.draw(surface)
        player.update()
        surface.fill('black')
        surface.blit(font_render,font_rec)
        keys=py.key.get_pressed()
        if keys[py.K_SPACE]:
            game=True
    py.display.update()