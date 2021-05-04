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
radius = 240
angle = 360
font = pygame.font.Font(None, 30)
color = 255,255,255
back = 176,178,250
color2 = 48,127,227
color3 = 128,170,160
blue_green = 13, 200, 186

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    today = datetime.datetime.today()
    hours = today.hour 
    minutes = today.minute
    seconds = today.second
    
    screen.fill(back)

    print_text(font, 0, 0, f"{today.hour}:{today.minute}")

    for n in range(1,13):
        angle = math.radians( n * (360/12) -90)
        x = math.cos( angle ) * (radius - 20) - 10
        y = math.sin( angle ) * (radius - 20) - 10
        print_text(font, pos_x+x, pos_y+y, str(n))

    # draw the hour hand
    hour_angle = wrap_angle( hours * (360/12)-90)
    hour_angle = math.radians(hour_angle)
    hour_x = math.cos(hour_angle) * (radius - 80)
    hour_y = math.sin(hour_angle) * (radius - 80)
    hour_target = (pos_x + hour_x, pos_y + hour_y)
    pygame.draw.line(screen, color2, (pos_x, pos_y), hour_target,25)
    
    # draw the minute hand
    minute_angle = wrap_angle(minutes * (360/60)-90)
    minute_angle = math.radians(minute_angle)
    minute_x = math.cos(minute_angle) * (radius - 60)
    minute_y = math.sin(minute_angle) * (radius - 60)
    minute_target = (pos_x + minute_x, pos_y + minute_y)
    pygame.draw.line(screen, color3, (pos_x,pos_y), minute_target, 12)

    # draw the second hand
    sec_angle = wrap_angle(seconds * (360/60) - 90)
    sec_angle = math.radians(sec_angle)
    sec_x = math.cos(sec_angle) * (radius-40)
    sec_y = math.sin(sec_angle) * (radius-40)
    sec_target = (pos_x+sec_x, pos_y+sec_y)
    pygame.draw.line(screen, blue_green, (pos_x,pos_y), sec_target, 6)

    pygame.draw.circle(screen, color, (pos_x,pos_y), 20)

    pos = ( int(pos_x + x), int(pos_y + y) )
    pygame.draw.circle(screen, color, (pos_x, pos_y), radius, 5)

    pygame.display.update()