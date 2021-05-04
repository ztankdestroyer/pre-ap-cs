import pygame 
from pygame.locals import*
pygame.init()
screen = pygame.display.set_mode((600,500)) 
pygame.display.set_caption("shape")
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((50,50,50))

    color = (0, 0, 0)
    size = (150, 150, 300, 200)

    ellipse = pygame.draw.ellipse(screen, color, size)

    pygame.display.update()
  

