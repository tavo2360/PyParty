import sys
import pygame,math,cmath
from pygame.locals import *
salir=False

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


#=======*Class that creates an invisible rectangle over the mouse*======
#=======================================================================
class Mouse(pygame.Rect):
	def __init__(self):						#Makes an invisible rectangle that follows the cursor
		pygame.Rect.__init__(self,0,0,1,1)
	def pos(self):						#Gets the cursor position
		(self.left, self.top) = pygame.mouse.get_pos()

#========================*Class for buttons*============================
#=======================================================================
class Buttons(pygame.sprite.Sprite):
	def __init__(self, pic1, pic2, x, y):
		self.imagen0=pic1
		self.imagen1=pic2
		self.imagenAct=self.imagen0
		self.rect=self.imagenAct.get_rect()
		self.rect.left,self.rect.top=(x,y)
                
	def update(self, screen, cursor):
		if cursor.colliderect(self.rect):
			self.imagenAct=self.imagen1
		else:
			self.imagenAct=self.imagen0
		screen.blit(self.imagenAct, self.rect)
                
#=========*Fuction to create the presentation windons*==================
#=======================================================================
def Windons():
	salirI=False
	pygame.init()
	screen = pygame.display.set_mode((1024,600))
	background = pygame.image.load("fondo1.jpg").convert()
	pygame.display.set_caption("PyPARTY")
	pygame.mixer.music.load("song1.mp3")
	screen.blit(background,(0,0))
	imagen1=pygame.image.load("gif.png")
	screen.blit(imagen1,(300,500))
	pygame.mixer.music.play(2)
	pygame.display.update()
  
	while salirI!= True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salirI=True
			if event.type == pygame.KEYDOWN:
				menu()
	pygame.quit()

#================*Fuction to create the menu windons*===================
#=======================================================================
def menu():
	join0 = pygame.image.load("join0.png")				#Load pictures for buttons
	join1 = pygame.image.load("join1.png")
	newgame0 = pygame.image.load("new game0.png")
	newgame1 = pygame.image.load("new game1.png")
	play0 = pygame.image.load("play0.png")
	play1 =  pygame.image.load("play1.png")
	
	cursor1=Mouse()										#Make a rectangle over the mouse
	
	bJoin = Buttons(join0, join1, 454, 403)				#Make the buttons
	bPlay = Buttons(play0, play1, 759,403)
	bNewGame = Buttons(newgame0, newgame1, 96, 403)

	lenghtW=0											#Variables for text
	texts = ''
	x=178
	screen=pygame.display.set_mode([1024,600])
	text=pygame.image.load("text.png")
	

	salirII=False
	pygame.init()
	screen = pygame.display.set_mode((1024,600))
	background = pygame.image.load("fondo2.jpg").convert()
	pygame.display.set_caption("PyPARTY")
	pygame.mixer.music.load("song2.mp3")
	screen.blit(background,(0,0))
	screen.blit(text, (23,76))
	pygame.mixer.music.play(2)
	pygame.display.update()


	while salirII!= True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:							#Event to exit
				return pygame.quit()
			elif event.type==pygame.KEYDOWN:											#Events for writing
				if event.key<=122 and event.key>=97 or event.key<=57 and event.key>=48:
					texts=texts+chr(event.key)
					lenghtW+=15
					x=x+15
					myfont= pygame.font.SysFont("Bradley Hand ITC",20, 1, 1)
					label=myfont.render(chr(event.key),1,black)
					screen.blit(label,(x,80))
					
				elif event.key == pygame.K_BACKSPACE:
					texts=texts[:-1]
					lenghtW-=15
					x=x-15
					myfont= pygame.font.SysFont("Bradley Hand ITC",20, 1, 1)
					label=myfont.render(texts,1,black)
					screen.blit(background, (0,0))
					screen.blit(text, (23,76))
					screen.blit(label,(178, 80))
		bJoin.update(screen, cursor1)
		bNewGame.update(screen, cursor1)
		bPlay.update(screen, cursor1)
		cursor1.pos()
		pygame.display.update()

Windons()




# ==========================================================================			
# Function to create a window
# ==========================================================================
def window(x, y):									  # Creates window where program runs
	pygame.init()									  
	screen = pygame.display.set_mode((x,y))
	screen.fill(black)
	pygame.display.update()	   
	return screen


# ==========================================================================
# Function to create board 
# ==========================================================================

def boardsquares(x,y,width,squarecolor,interval,startcolor,orientation,border,bordercolor):
	square=pygame.draw.rect(screen,
					 squarecolor,
					 (x,y,width,width),0)
	square=pygame.draw.rect(screen,
					 bordercolor,
					 (x,y,width,width),border)
	if orientation=="horizontal":
		if startcolor==blue:
			if interval > 0:
				interval -= 1
				boardsquares(x+width,y,width,green,interval,startcolor,orientation,border,bordercolor)
			if interval > 0:
				interval -= 1
				boardsquares(x+2*width,y,width,red,interval,startcolor,orientation,border,bordercolor)
			if interval > 0:
				interval -= 1
				boardsquares(x+3*width,y,width,blue,interval,startcolor,orientation,border,bordercolor)
		if startcolor==green:
			if interval > 0:
				interval -= 1
				boardsquares(x+width,y,width,red,interval,startcolor,orientation,border,bordercolor)
			if interval > 0:
				interval -= 1
				boardsquares(x+2*width,y,width,blue,interval,startcolor,orientation,border,bordercolor)
			if interval > 0:
				interval -= 1
				boardsquares(x+3*width,y,width,green,interval,startcolor,orientation,border,bordercolor)
		if startcolor==red:
			if interval > 0:
				interval -= 1
				boardsquares(x+width,y,width,blue,interval,startcolor,orientation,border,bordercolor)
			if interval > 0:
				interval -= 1
				boardsquares(x+2*width,y,width,green,interval,startcolor,orientation,border,bordercolor)
			if interval > 0:
				interval -= 1
				boardsquares(x+3*width,y,width,red,interval,startcolor,orientation,border,bordercolor)
	if orientation=="vertical":
		if startcolor==blue:
			if interval > 0:
				interval -= 1
				boardsquares(x,y+width,width,green,interval,startcolor,orientation,border,bordercolor)
			if interval > 0:
				interval -= 1
				boardsquares(x,y+2*width,width,red,interval,startcolor,orientation,border,bordercolor)
			if interval > 0:
				interval -= 1
				boardsquares(x,y+3*width,width,blue,interval,startcolor,orientation,border,bordercolor)
		if startcolor==green:
			if interval > 0:
				interval -= 1
				boardsquares(x,y+width,width,red,interval,startcolor,orientation,border,bordercolor)
			if interval > 0:
				interval -= 1
				boardsquares(x,y+2*width,width,blue,interval,startcolor,orientation,border,bordercolor)
			if interval > 0:
				interval -= 1
				boardsquares(x,y+3*width,width,green,interval,startcolor,orientation,border,bordercolor)
		if startcolor==red:
			if interval > 0:
				interval -= 1
				boardsquares(x,y+width,width,blue,interval,startcolor,orientation,border,bordercolor)
			if interval > 0:
				interval -= 1
				boardsquares(x,y+2*width,width,green,interval,startcolor,orientation,border,bordercolor)
			if interval > 0:
				interval -= 1
				boardsquares(x,y+3*width,width,red,interval,startcolor,orientation,border,bordercolor)

# ==========================================================================
# Function to create board window
# ==========================================================================

def boardwindow():
	global screen
	done=1
	screen = window(749, 468) 
	pygame.display.set_caption("PyParty Board")
	screen.fill(black)
	boardsquares(200,20,50,blue,5,blue,"horizontal",2,black)
	boardsquares(156,22,46,blue,0,blue,"horizontal",2,blue)
	boardsquares(116,22,46,blue,0,blue,"horizontal",2,blue)
	boardsquares(100,22,46,blue,0,blue,"horizontal",2,blue)
	boardsquares(100,60,46,blue,0,blue,"horizontal",2,blue)
	boardsquares(100,95,46,blue,0,blue,"horizontal",2,blue)
	boardsquares(500,370,-50,green,6,green,"horizontal",2,black)
	boardsquares(500,20,50,blue,6,blue,"vertical",2,black)
	boardsquares(150,370,-50,red,4,red,"vertical",2,black)
	boardsquares(100,95,46,blue,0,blue,"horizontal",2,blue)
	#shortcut5 to 20
	boardsquares(400,70,50,red,3,red,"vertical",8,yellow)
	boardsquares(400,270,-50,blue,4,blue,"horizontal",8,yellow)
	boardsquares(150,270,50,red,0,red,"horizontal",8,yellow)
	#shortcut5 to 15
	boardsquares(415,85,20,red,0,red,"vertical",8,purple)
	boardsquares(400,120,-50,blue,2,blue,"horizontal",8,purple)
	boardsquares(250,120,50,blue,3,blue,"vertical",8,purple)
	boardsquares(300,270,50,green,1,green,"horizontal",8,purple)
	boardsquares(400,270,50,red,0,red,"horizontal",8,purple)
	#shorcut10 to 12
	boardsquares(550,170,50,blue,2,blue,"vertical",8,white)
	pygame.display.flip()
	while done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				pygame.quit();sys.exit();


boardwindow()
