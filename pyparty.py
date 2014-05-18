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
<<<<<<< HEAD

# ==========================================================================			
# Function to create a window
# ==========================================================================
def window(x, y):									  # Creates window where program runs
	pygame.init()									  
	screen = pygame.display.set_mode((x,y))
	background = pygame.image.load("background.jpg").convert()		#opens background image
	pygame.display.set_caption("Figure Maker ADVANCED 2")
	screen.blit(background,(0,0))
	pygame.display.update()	   
	return screen
	

# ==========================================================================
# Function to create buttons
# ==========================================================================
def Button(screen, x, y, width, text, buttonColor, textColor):	   #creats buttons
	font=pygame.font.Font(None,24)								   #choses font size
	rect=pygame.draw.rect(screen, black, (x,y,width,30), 1)		   #button shape
	screen.fill(buttonColor, rect)
	screen.blit(font.render(text, True, textColor), (x+20, y+7))
	pygame.display.update()
	return [rect, text]
	
# ==========================================================================
# Function to create board 
# ==========================================================================

def boardsquares(x,y,width,squarecolor,interval,startcolor,orientation):
	square=pygame.draw.rect(screen,
					 squarecolor,
					 (x,y,width,width),0)
	square=pygame.draw.rect(screen,
					 black,
					 (x,y,width,width),2)
	if orientation=="horizontal":
		if startcolor==blue:
			if interval > 0:
				interval -= 1
				boardsquares(x+width,y,width,green,interval,startcolor,orientation)
			if interval > 0:
				interval -= 1
				boardsquares(x+2*width,y,width,red,interval,startcolor,orientation)
			if interval > 0:
				interval -= 1
				boardsquares(x+3*width,y,width,blue,interval,startcolor,orientation)
		if startcolor==green:
			if interval > 0:
				interval -= 1
				boardsquares(x+width,y,width,red,interval,startcolor,orientation)
			if interval > 0:
				interval -= 1
				boardsquares(x+2*width,y,width,blue,interval,startcolor,orientation)
			if interval > 0:
				interval -= 1
				boardsquares(x+3*width,y,width,green,interval,startcolor,orientation)
		if startcolor==red:
			if interval > 0:
				interval -= 1
				boardsquares(x+width,y,width,blue,interval,startcolor,orientation)
			if interval > 0:
				interval -= 1
				boardsquares(x+2*width,y,width,green,interval,startcolor,orientation)
			if interval > 0:
				interval -= 1
				boardsquares(x+3*width,y,width,red,interval,startcolor,orientation)
	if orientation=="vertical":
		if startcolor==blue:
			if interval > 0:
				interval -= 1
				boardsquares(x,y+width,width,green,interval,startcolor,orientation)
			if interval > 0:
				interval -= 1
				boardsquares(x,y+2*width,width,red,interval,startcolor,orientation)
			if interval > 0:
				interval -= 1
				boardsquares(x,y+3*width,width,blue,interval,startcolor,orientation)
		if startcolor==green:
			if interval > 0:
				interval -= 1
				boardsquares(x,y+width,width,red,interval,startcolor,orientation)
			if interval > 0:
				interval -= 1
				boardsquares(x,y+2*width,width,blue,interval,startcolor,orientation)
			if interval > 0:
				interval -= 1
				boardsquares(x,y+3*width,width,green,interval,startcolor,orientation)
		if startcolor==red:
			if interval > 0:
				interval -= 1
				boardsquares(x,y+width,width,blue,interval,startcolor,orientation)
			if interval > 0:
				interval -= 1
				boardsquares(x,y+2*width,width,green,interval,startcolor,orientation)
			if interval > 0:
				interval -= 1
				boardsquares(x,y+3*width,width,red,interval,startcolor,orientation)

# ==========================================================================
# Function to create board window
# ==========================================================================

def boardwindow():
	global screen
	done=1
	screen = window(749, 468) 
	pygame.display.set_caption("PyParty Board")
	screen.fill(black)
	boardsquares(150,20,50,blue,6,blue,"horizontal")
	boardsquares(150,370,50,blue,6,blue,"horizontal")
	boardsquares(500,20,50,green,7,green,"vertical")
	pygame.display.flip()
	while done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				pygame.quit();sys.exit();
	

boardwindow()






=======
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
>>>>>>> 0089821d6e0c9590ea30b061a7788090ac465fae

