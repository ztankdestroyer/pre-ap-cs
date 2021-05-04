import sys, random, math, pygame
from pygame. locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Orbit Demo")

pos_x = 400
pos_y = 300
radius = 200
angle = 360
space = pygame.image.load("space.png").convert_alpha( )
planet = pygame.image.load("planet2.png").convert_alpha( )
ship = pygame.image.load("freelance.png").convert_alpha( )
width, height = ship.get_size()
ship = pygame.transform.scale(ship, (width//2, height//2))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    
    angle += .05
    if angle >= 360:
        angle = 0
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color = r,g,b
    
    x = math.cos( math.radians(angle) ) * radius
    y = math.sin( math.radians(angle) ) * radius
    
    ship_new = pygame.transform.rotate(ship, -1 *(angle + 90))

    width1, height1 = ship_new.get_size()
    

    pos = ( int(pos_x + x - (width1/2)), int(pos_y + y - (height1/2)) )
    

    width,height = planet.get_size()

    screen.blit(space, (0,0))
    screen.blit(planet, (400-width/2,300-height/2))
    screen.blit(ship_new, (pos))

    pygame.display.update()