import sys, random, math, pygame, datetime
from pygame. locals import *

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("circle demo")
screen.fill((0,0, 100))

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

def wrap_angle(angle):
    return abs(angle % 360)

pos_x = 300
pos_y = 250
radius = 200
angle = 360
font = pygame.font.Font(None, 30)
color = 255,255,255
pink = 255, 192, 203
orange = 255, 215, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    today = datetime.datetime.today()
    hours = today.hour % 12
    
    for n in range(1,13):
        angle = math.radians( n * (360/12) -90)
        x = math.cos( angle ) * (radius - 20) - 10
        y = math.sin( angle ) * (radius - 20) - 10
        print_text(font, pos_x+x, pos_y+y, str(n))

    hour_angle = wrap_angle( hours * (360/12)-90)
    hour_angle = math.radians(hour_angle)
    hour_x = math.cos(hour_angle) * (radius - 80)
    hour_y = math.sin(hour_angle) * (radius - 80)
    min_angle = wrap_angle(minutes * (360/60) - 90)
    min_angle = math.radians( min_angle )
    min_x = math.cos( min_angle ) * (radius - 60)
    min_y = math.sin( min_angle ) * (radius - 60)
    target = (pos_x + min_x, pos_y + min_y) 
    target = (pos_x + hour_x, pos_y + hour_y)

    pygame.draw.line(screen, pink, (pos_x, pos_y), target,25)
    pygame.draw.line(screen, orange, (pos_x, pos_y), target, 12)
    
    pos = ( int(pos_x + x), int(pos_y + y) )
    pygame.draw.circle(screen, color, (pos_x, pos_y), 210, 5)
    pygame.draw.circle(screen, color, (pos_x, pos_y), 15, 25)

    pygame.display.update()