import pygame 
from pygame.locals import*
pygame.init()
screen = pygame.display.set_mode((600,500)) 
pygame.display.set_caption("snowman")
while True:
  for event in pygame.event.get():
    if event.type in (QUIT, KEYDOWN):
      sys.exit()
  
  screen.fill((50,50,50))

  #arm 1
  color2 = (165, 42, 42)
  width = 8
  pos1 = 150, 100
  pos2 = 300, 230
  pygame.draw.line(screen, color2, pos1, pos2, width)

  #arm 2
  color2 = (165, 42, 42)
  width = 8
  pos3 = 350, 200
  pos4 = 450, 300
  pygame.draw.line(screen, color2, pos3, pos4, width)

  #circle 1
  color1 = 255,255,255
  position1 = 300, 350
  radius1 = 80
  width1 = 0
  pygame.draw.circle(screen, color1, position1, radius1, width1)

  #circle 2
  color1 = 255,255,255
  position2 = 300, 220
  radius2 = 65
  width2 = 0
  pygame.draw.circle(screen, color1, position2, radius2, width2)

  #circle 3
  color1 = 255,255,255
  position3 = 300, 130
  radius3 = 40
  width3 = 0
  pygame.draw.circle(screen, color1, position3, radius3, width3)

  #eye 1
  color1 = 0,0,0
  position3 = 290, 120
  radius3 = 5
  width3 = 0
  pygame.draw.circle(screen, color1, position3, radius3, width3)

  #eye 2
  color1 = 0,0,0
  position4 = 310, 120
  radius3 = 5
  width3 = 0
  pygame.draw.circle(screen, color1, position4, radius3, width3)
    #button 3
  color1 = 0,0,0
  position3 = 300, 190
  radius3 = 5
  width3 = 0
  pygame.draw.circle(screen, color1, position3, radius3, width3)
    #button2
  color1 = 0,0,0
  position3 = 300, 250
  radius3 = 5
  width3 = 0
  pygame.draw.circle(screen, color1, position3, radius3, width3)
    #button 1
  color1 = 0,0,0
  position3 = 300, 310
  radius3 = 5
  width3 = 0
  pygame.draw.circle(screen, color1, position3, radius3, width3)

  #nose
  color1 = 255,165,0
  position3 = 300, 130
  radius3 = 5
  width3 = 0
  pygame.draw.circle(screen, color1, position3, radius3, width3)

  #mouth
  color5 = 0,0,0
  x = 280
  y = 140
  width = 30
  height = 10
  start_angle = 0
  stop_angle = 180
  thickness = 3
  pygame.draw.arc(screen, color5, (x,y,width,height), start_angle, stop_angle, thickness)

  #hat part 1
  color1 = 0,0,0
  width1 = 20
  pos5 = 300, 100
  pos6 = 300, 80
  pygame.draw.line(screen, color1, pos5, pos6, width1)




  pygame.display.update()