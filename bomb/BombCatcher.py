
import sys, random, time, math, pygame
from pygame.locals import *
from pygame import mixer 

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))
    

#main program begins
pygame.init()
mixer.init()
mixer.music.load("boom.wav")
huston_Bomb = pygame.image.load("bomb.png")
huston_Bomb = pygame.transform.scale(huston_Bomb, (50,50))
mixer.music.set_volume(0.7)
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Modified Bomb Catching Game")
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 40)
pygame.mouse.set_visible(False)
white = 255,255,255
red = 220, 50, 50
yellow = 230,230,50
black = 0,0,0
pi = 3.141592653

lives = 0
score = 0
clock_start = 0
game_over = True
mouse_x = mouse_y = 0

pos_x = 300
pos_y = 460

bomb_x = random.randint(0,500)
vel_x = ((random.randrange(-1000,1000))/2000)
bomb_y = -50
vel_y = 0.2

game_over = True
clock_start = 0
seconds = 1

#repeating loop
while True:
    current = time.time() - clock_start
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = event.pos
            move_x,move_y = event.rel
        elif event.type == MOUSEBUTTONUP:
            if game_over:
                print_text(font1, 100, 200, "<CLICK TO PLAY>") 
                if game_over:
                    game_over = False
                    score = 0
                    seconds = 2
                    clock_start = time.time()
                    lives = 3
                    score = 0
                    print_text(font1, 0, 80, "Time: " + str(int(seconds-current)))
                

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    
    

    screen.fill((0,0,100))

    

    if game_over:
        print_text(font1, 100, 200, "<CLICK TO PLAY>") 
    else:
        #move the bomb
        bomb_y += vel_y
        bomb_x += vel_x 
        screen.blit(huston_Bomb, (bomb_x - 25, bomb_y - 25))

        if bomb_x > 585 or bomb_x< 30:
            vel_x = -vel_x


        #has the player missed the bomb?
        if bomb_y > 500:
            print_text(font2, 300, 250, "Boom!", red)
            pygame.display.update()
            time.sleep(1)
            bomb_x = random.randint(0, 500)
            bomb_y = -50
            lives -= 1
            mixer.music.play()
            if lives == 0:
                game_over = True

        #see if player has caught the bomb
        elif bomb_y > pos_y:
            if bomb_x > pos_x and bomb_x < pos_x + 120:
                score += 10
                bomb_x = random.randint(0, 500)
                bomb_y = -50
        
        #draw the bomb
        pygame.draw.arc(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (bomb_x, int(bomb_y) - 50, 50, 50), 1, 3,5)
        

        #set basket position
        pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 500:
            pos_x = 500
        #draw basket
        pygame.draw.rect(screen, black, (pos_x-4,pos_y-4,120,40), 0)
        pygame.draw.rect(screen, red, (pos_x,pos_y,120,40), 0)

    #print # of lives
    print_text(font1, 0, 0, "LIVES: " + str(lives))

    #print score
    print_text(font1, 500, 0, "SCORE: " + str(score))
    
    pygame.display.update()
