import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('boogers')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('bigger boogers', False, GREEN)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

soundObj = pygame.mixer.Sound('beep1.ogg')
import time

pygame.mixer.music.load('tetrisb.mid')
pygame.mixer.music.play(-1, 0.0)

while True: # main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    soundObj.play()
    
    #import time
    time.sleep(0)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            #pygame.mixer.music.stop()
    pygame.display.update()
