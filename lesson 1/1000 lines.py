import pygame 
import random
from pygame.locals import*
pygame.init()
screen = pygame.display.set_mode((600,500)) 
pygame.display.set_caption("snowman")
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
  
    screen.fill((50,50,50))

    for i in range(1000):
        color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        width = 1
        pos1 = random.randint(0,600), random.randint(0,500)
        pos2 = random.randint(0,600), random.randint(0,500)
        pygame.draw.line(screen, color2, pos1, pos2, width)

    pygame.display.update()