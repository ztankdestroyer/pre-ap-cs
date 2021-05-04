import pygame
from pygame.locals import *
import random
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Bouncing logo")
dvd = pygame.image.load("dvd.png")

pos_x = 300
pos_y = 250
vel_x = .4
vel_y = .2
x=1
while True:
  for event in pygame.event.get():
    if event.type in (QUIT, KEYDOWN):
      sys.exit()

  screen.fill((0,0,200))

  pos_x += vel_x
  pos_y += vel_y

  if pos_x > 420 or pos_x< 0:
    vel_x = -vel_x
    color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    x=0
  if pos_y > 370 or pos_y< 0:
    vel_y = -vel_y
    color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    x=0
  if x == 1:
    color = 255,255,0
  width = 0
  pos = pos_x, pos_y, 100, 100
  screen.blit(dvd, (pos))

  pygame.display.update()