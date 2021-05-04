# Escape The Dragon Game

import sys, time, random, math, pygame
from pygame.locals import *

class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self) #extend the base Sprite class
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

    #X property
    def _getx(self): return self.rect.x
    def _setx(self,value): self.rect.x = value
    X = property(_getx,_setx)

    #Y property
    def _gety(self): return self.rect.y
    def _sety(self,value): self.rect.y = value
    Y = property(_gety,_sety)

    #position property
    def _getpos(self): return self.rect.topleft
    def _setpos(self,pos): self.rect.topleft = pos
    position = property(_getpos,_setpos)
        

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0,0,width,height)
        self.columns = columns
        #try to auto-calculate total frames
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=30):
        #update animation frame number
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        #build current frame only if it changed
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + \
               "," + str(self.last_frame) + "," + str(self.frame_width) + \
               "," + str(self.frame_height) + "," + str(self.columns) + \
               "," + str(self.rect)


def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

def reset_arrow():
    y = random.randint(250,350)
    arrow.position = 800,y

#main program begins
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Escape The Dragon Game")
font = pygame.font.Font(None, 18)
framerate = pygame.time.Clock()
hit = 0
miss = 0

#load bitmaps
bg = pygame.image.load("background.png").convert_alpha()

#create a sprite group
group = pygame.sprite.Group()

#create the dragon sprite
dragon = MySprite(screen)
dragon.load("dragon.png", 260, 150, 3)
dragon.position = 100, 230
group.add(dragon)

#create the player sprite
player = MySprite(screen)
player.load("caveyboy.png", 51, 67, 8)
player.first_frame = 0
player.last_frame = 7
player.position = 400, 303
group.add(player)

#create the arrow sprite
arrow = MySprite(screen)
arrow.load("flame.png", 40, 16, 1)
arrow.position = 800,320
group.add(arrow)

arrow_vel = 8.0
game_over = False
you_win = False
player_jumping = False
jump_vel = 0.0
big_jump_vel = 0.0
player_start_y = player.Y

done=False

#repeating loop
while not done:
    framerate.tick(30)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == QUIT: done=True
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: done=True
    if player.Y > 100:
        if keys[K_SPACE]:
            jump_accel=.2
            if not player_jumping:
                player_jumping = True
                jump_vel = -8.0
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_SPACE]:
                    jump_vel = -8.0
                    player.frame = 7
                    player.first_frame = 8
                    player.last_frame = 11
                

        else:
            jump_accel=.5
    


    #update the arrow
    if not game_over:
        arrow.X -= arrow_vel
        if arrow.X < -40: reset_arrow()

    #did arrow hit player?
    if pygame.sprite.collide_rect(arrow, player):
        reset_arrow()
        player.X -= 10
        hit += 1

    #did arrow hit dragon?
    if pygame.sprite.collide_rect(arrow, dragon):
        reset_arrow()
        dragon.X -= 10
        miss += 1

    #did dragon eat the player?
    if pygame.sprite.collide_rect(player, dragon):
        game_over = True
        miss = 0
        hit = 0

    #did the dragon get defeated?
    if dragon.X < -100:
        you_win = True
        game_over = True
        miss = 0
        hit = 0

    #is the player jumping?
    if player_jumping:
        player.first_frame = 8
        player.last_frame = 11
        player.Y += jump_vel
        jump_vel += jump_accel
        if player.Y > player_start_y:
            player_jumping = False
            player.Y = player_start_y
            jump_vel = 0.0
    if player_jumping == False:
        player.first_frame = 0
        player.last_frame = 7


    #draw the background
    screen.blit(bg, (0,0))

    #update sprites
    if not game_over:
        group.update(ticks, 50)

    #draw sprites
    group.draw(screen)

    print_text(font, 350, 560, "Press SPACE to jump!")

    print_text(font, 0, 0, "Times hit: " + str(hit))
    print_text(font, 0, 20, "Times evaded: " + str(miss))

    if game_over:
        print_text(font, 360, 100, "G A M E   O V E R")
        if you_win:
            print_text(font, 330, 130, "YOU BEAT THE DRAGON!")
        else:
            print_text(font, 330, 130, "THE DRAGON GOT YOU!")

    
    pygame.display.update()
    
