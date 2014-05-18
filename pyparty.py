import sys
import pygame,math,cmath
from pygame.locals import *
flag=True

def Windons():
  pygame.init()
  screen = pygame.display.set_mode((1024,600))
  background = pygame.image.load("background.jpg").convert()
  pygame.mixer.music.load("presentation.mp3")
  pygame.display.set_caption("PyPARTY")
  screen.blit(background,(0,0))
  pygame.display.update()
  return screen
  pygame.mixer.music.play(2)
  while (flag):
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();

Windons()














# ==========================================================================
# Color's definition
# ==========================================================================

yellow=(255,238,0)									  
blue=(0,107,179)
darkBlue=(24,41,131)
lightBlue=(0,157,226)
fuchsia=(255,0,128)
purple=(147,17,126)
orange=(255,153,51)
lightRed=(227,0,79)
red=(227,0,35)
pink=(225,0,122)
lightGreen=(151,190,13)
green=(0,145,54)
white=(255,255,255)
black=(0,0,0)
##
### ==========================================================================			
### Function to create a window
### ==========================================================================
##def window(x, y):									  # Creates window where program runs
##	pygame.init()									  
##	screen = pygame.display.set_mode((x,y))
##	background = pygame.image.load("background.jpg").convert()		#opens background image
##	pygame.display.set_caption("Figure Maker ADVANCED 2")
##	screen.blit(background,(0,0))
##	pygame.display.update()	   
##	return screen
##	
##
### ==========================================================================
### Function to create buttons
### ==========================================================================
##def Button(screen, x, y, width, text, buttonColor, textColor):	   #creats buttons
##	font=pygame.font.Font(None,24)								   #choses font size
##	rect=pygame.draw.rect(screen, black, (x,y,width,30), 1)		   #button shape
##	screen.fill(buttonColor, rect)
##	screen.blit(font.render(text, True, textColor), (x+20, y+7))
##	pygame.display.update()
##	return [rect, text]

