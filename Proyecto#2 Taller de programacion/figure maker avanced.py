#===========================================================================
###########################--Figure Maker--#################################
#===========================================================================


import sys
import pygame,math,cmath
from pygame.locals import *
fractal_level = 4
# ==========================================================================
# Color's definition
#############################################################################
#In this part we defined the color that we gone use
#############################################################################
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
# ==========================================================================
# Events handler flags
#############################################################################
#The flags we used for stop a proces a continue whit other
#############################################################################
# ==========================================================================
eventsFlagI = True									  #when eventsFlagI is true
eventsFlagII = True									  #when eventsFlagII is true
eventsFlagIII = True								  #when eventsFlagIII is true
eventsFlagIV = True
done = True
# ==========================================================================			
# Function to create a window
#############################################################################
#fuction for make the principal Window, here we defined the background and
#the title of the windonw
#############################################################################
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
# Functions to main windows
#############################################################################
#any event was defined here
#############################################################################
# ==========================================================================
def addEvent(event, rect, text):
	if event.type==pygame.MOUSEBUTTONDOWN:			  #if mousebutton is touched 
		pos = pygame.mouse.get_pos()				  
		if rect.collidepoint(pos):
			eventsFlagI = False			
			if text == "Normals":					  #open selectnormals
				selectNormals(text)
			elif text == "Fractals":				  #open selectfractals
				selectFractals(text)
# ==========================================================================
# Functions to main windows
# ==========================================================================
def addEventnormal(event, rect, text):				  #when mouse selects an option from selectnormals open selectnormalsattributes
	if event.type==pygame.MOUSEBUTTONDOWN:
		pos = pygame.mouse.get_pos()
		if rect.collidepoint(pos):
			selectNormalsAttributes(text)
				
# ==========================================================================
# Functions to main windows
# ==========================================================================
def addEventFractal(event, rect, text):				  #when mouse selects an option from selectfractal open selectfractalattributes
	if event.type==pygame.MOUSEBUTTONDOWN:
		pos = pygame.mouse.get_pos()
		if rect.collidepoint(pos):
			selectfractalsAttributes(text)

# ==========================================================================
# Functions to the colors of normal windons
# ==========================================================================
def addEventII(event, rect, textButton, textFigure,screen):		 # what happens when each color is selected
	if event.type==pygame.MOUSEBUTTONDOWN:		  
		pos = pygame.mouse.get_pos()
		if rect.collidepoint(pos):
			global selectedColor
			if textButton != "Look what you've done!":#that make the push efect in the bottons colors and call the figure that you chooise
				if textButton == "Dark Blue":
					selectedColor = darkBlue;
					darkBlueButton = Button(screen, 310, 140, 120, "Dark Blue", blue, black)
				elif textButton != "Dark Blue":
					darkBlueButton = Button(screen, 313, 145, 120, "",blue, black)
					darkBlueButton = Button(screen, 310, 140, 120, "Dark Blue",lightBlue, black)
					
				if textButton == "Blue":
					selectedColor = blue;
					blueButton = Button(screen, 310, 100, 120, "Blue", blue, black)
				elif textButton != "Blue":
					blueButton = Button(screen, 313, 105, 120, "", blue, black)
					blueButton = Button(screen, 310, 100, 120, "Blue", lightBlue, black)
					
				if textButton == "Yellow":
					selectedColor = yellow;
					yellowButton = Button(screen, 310, 60, 120, "Yellow", blue, black)
				elif textButton != "Yellow":				   
					yellowButton = Button(screen, 313, 65, 120, "", blue, black)
					yellowButton = Button(screen, 310, 60, 120, "Yellow", lightBlue, black)
					
				if textButton == "Purple":
					selectedColor = purple;
					purpleButton = Button(screen, 450, 60, 120, "Purple", blue, black)
				elif textButton!="Purple":
					purpleButton = Button(screen, 453, 65, 120, "", blue, black)
					purpleButton = Button(screen, 450, 60, 120, "Purple", lightBlue, black)
					
				if textButton == "Light Blue":
					selectedColor = lightBlue;
					lightBlueButton = Button(screen, 310, 180, 120, "Light Blue", blue, black)
				elif textButton !="Light Blue":
					lightBlueButton = Button(screen, 313, 185, 120, "", blue, black)
					lightBlueButton = Button(screen, 310, 180, 120, "Light Blue",lightBlue, black)
					
				if textButton == "Light Red":
					selectedColor = lightRed;
					lightRedButton = Button(screen, 450, 140, 120, "Light Red", blue, black)
				elif textButton!="Light Red":
					lightRedButton = Button(screen, 453, 145, 120, "", blue, black)
					lightRedButton = Button(screen, 450, 140, 120, "Light Red", lightBlue, black)
				if textButton == "Orange":
					selectedColor = orange;
					orangeButton = Button(screen, 450, 100, 120, "Orange", blue, black)
				elif textButton!="Orange":
					orangeButton = Button(screen, 453, 105, 120, "", blue, black)
					orangeButton = Button(screen, 450, 100, 120, "Orange", lightBlue, black)
					
				if textButton == "Red":
					selectedColor = red ;
					redButton = Button(screen, 450, 180, 120, "Red", blue, black)
				elif textButton!="Red":
					redButton = Button(screen, 453, 185, 120, "",  blue, black)
					redButton = Button(screen, 450, 180, 120, "Red", lightBlue, black)
					
				if textButton == "Fuchsia":
					selectedColor = fuchsia;
					fuchsiaButton = Button(screen, 590, 140, 120, "Fuchsia", blue, black)
				elif textButton !="Fuchsia":
					fuchsiaButton = Button(screen, 593, 145, 120, "", blue, black)
					fuchsiaButton = Button(screen, 590, 140, 120, "Fuchsia", lightBlue, black)
					
				if textButton == "Pink":
					selectedColor = pink;
					pinkButton = Button(screen, 590, 220, 120, "Pink", blue, black)
				elif textButton !="Pink":
					pinkButton = Button(screen, 593, 225, 120, "", blue, black)
					pinkButton = Button(screen, 590, 220, 120, "Pink", lightBlue, black)
					
				if textButton == "Light Green":
					selectedColor = lightGreen;
					lightGreenButton = Button(screen, 590, 60, 120, "Light Green", blue, black)
				elif textButton!="Light Green":
					lightGreenButton = Button(screen, 593, 65, 120, "", blue, black)
					lightGreenButton = Button(screen, 590, 60, 120, "Light Green", lightBlue, black)		
				if textButton == "Green":
					selectedColor = green;
					greenButton = Button(screen, 590, 100, 120, "Green", blue, black)
				elif textButton!= "Green":
					greenButton = Button(screen, 593, 105, 120, "", blue, black)
					greenButton = Button(screen, 590, 100, 120, "Green", lightBlue, black)					  
				if textButton == "Black":
					selectedColor = black;
					blackButton = Button(screen, 590, 180, 120, "Black", blue, black)
				elif textButton!="Black":
					blackButton = Button(screen, 593, 185, 120, "", blue, black)
					blackButton = Button(screen, 590, 180, 120, "Black", lightBlue, black)
			else:
				global radius1# some global variable
				global side1
				radius1=80
				side1=150
				drawFigure(selectedColor, textFigure,radius1,side1)


					

# ==========================================================================
# Functions to draw the figures
# ==========================================================================

def addEventIII(event,rect,text,screen):
	if event.type==pygame.MOUSEBUTTONDOWN:		  
		pos = pygame.mouse.get_pos()
		if rect.collidepoint(pos):
			pygame.image.save(screen,string)
# ==========================================================================
# Functions to return at the main windonw
# ==========================================================================
def addEventmain(event,rect,text):
	if event.type==pygame.MOUSEBUTTONDOWN:		  
		pos = pygame.mouse.get_pos()
		if rect.collidepoint(pos):
			main()
# ==========================================================================
# Functions to change the size of the figures
# ==========================================================================
def addEventaddsize(event,rect,text,figure,screen):
	if event.type==pygame.MOUSEBUTTONDOWN:		  
		pos = pygame.mouse.get_pos()
		if rect.collidepoint(pos):
			global radius1
			global side1
			if figure=="Circle":
				if radius1+10<=130:
					radius1=radius1+10
					drawFigure(selectedColor, figure,radius1,side1)
				else:
					drawFigure(selectedColor, figure,radius1,side1)
			if figure=="Square":
				if side1+25<=325:
					side1=side1+25
					drawFigure(selectedColor, figure,radius1,side1)
				else:
					drawFigure(selectedColor, figure,radius1,side1)
			if figure == "Rectangle":
					drawFigure(selectedColor, figure,radius1,side1)					   
def addEventsize(event,rect,text,figure,screen):
	if event.type==pygame.MOUSEBUTTONDOWN:		  
		pos = pygame.mouse.get_pos()
		if rect.collidepoint(pos):
			global radius1
			global side1
			if figure=="Circle":
				if radius1-10>=10:
					radius1=radius1-10
					drawFigure(selectedColor, figure,radius1,side1)
				else:
					drawFigure(selectedColor, figure,radius1,side1)
			if figure=="Square":
				if side1-25>=25:
					side1=side1-25
					drawFigure(selectedColor, figure,radius1,side1)
				else:
					drawFigure(selectedColor, figure,radius1,side1)
			if figure == "Rectangle":
					drawFigure(selectedColor, figure,radius1,side1)

# ==========================================================================
# Function to change the size of the fractals
# ==========================================================================
def addEventaddsizefractal(event,rect,selectedColor, textFigure,background):
	if event.type==pygame.MOUSEBUTTONDOWN:		  
		pos = pygame.mouse.get_pos()
		if rect.collidepoint(pos):
			global fractal_level
			fractal_level=fractal_level+1
			if fractal_level>0 and fractal_level<7:
				drawfractal(selectedColor, textFigure,background)
			
									 
def addEventsizefractal(event,rect,selectedColor, textFigure,background):
	if event.type==pygame.MOUSEBUTTONDOWN:		  
		pos = pygame.mouse.get_pos()
		if rect.collidepoint(pos):
			global fractal_level
			fractal_level = fractal_level-1
			if fractal_level>0 and fractal_level<7:
			 drawfractal(selectedColor, textFigure,background)

# ==========================================================================
# Function to create buttons
# ==========================================================================
c=0
			
def addEventsave(event,rect,text,screen):
	global c
	c=c+1
	if event.type==pygame.MOUSEBUTTONDOWN:		  
		pos = pygame.mouse.get_pos()
		if rect.collidepoint(pos):
			string="Figuras Guardadas\Figura"+str(c)+".png"
			pygame.image.save(screen,string)

			


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
# First window functionality
# ==========================================================================
def main():													   #main window
	screen = window(749, 468)								   #main window size
	font=pygame.font.Font(None,30)
	mainText = font.render('Welcome at the Figure maker ADVANCED2', True, darkBlue)
	screen.blit(mainText, (300,20))
	mainText = font.render('Select the type of figures:', True, darkBlue)
	screen.blit(mainText, (300,50))
	NormalButton = Button(screen, 523, 150, 150, '', blue, black)
	NormalButton = Button(screen, 520, 147, 150, 'Normals', lightBlue, black)
	FractalButton = Button(screen, 323, 150, 150, '', blue, black)
	FractalButton = Button(screen, 320, 147, 150, 'Fractals', lightBlue, black)
	while (eventsFlagI):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				 pygame.quit(); sys.exit();
			addEvent(event, NormalButton[0], NormalButton[1])	#if normal is selected
			addEvent(event, FractalButton[0], FractalButton[1]) #if fractal is selected
# ==========================================================================
# Windonws tho choose colors of normal selection
# ==========================================================================
def selectNormalsAttributes(text):
	screen = window(749, 468)
	font=pygame.font.Font(None,30)
	secondaryText = font.render('Select color and size for the '+ text, True, darkBlue)
	screen.blit(secondaryText, (310,20))

	# Here should be the inputs or buttons to choose color and size.
	yellowButton = Button(screen, 313, 65, 120, "", blue, black)
	yellowButton = Button(screen, 310, 60, 120, "Yellow", lightBlue, black)
	blueButton = Button(screen, 313, 105, 120, "", blue, black)
	blueButton = Button(screen, 310, 100, 120, "Blue", lightBlue, black)
	darkBlueButton = Button(screen, 313, 145, 120, "", blue, black)
	darkBlueButton = Button(screen, 310, 140, 120, "Dark Blue", lightBlue, black)
	lightBlueButton = Button(screen, 313, 185, 120, " ", blue, black)
	lightBlueButton = Button(screen, 310, 180, 120, "Light Blue",lightBlue, black)
	purpleButton = Button(screen, 453, 65, 120, "", lightBlue, black)
	purpleButton = Button(screen, 450, 60, 120, "Purple", lightBlue, black)
	orangeButton = Button(screen, 453, 105, 120, "", blue, black)
	orangeButton = Button(screen, 450, 100, 120, "Orange", lightBlue, black)
	lightRedButton = Button(screen, 453, 145, 120, "", blue, black)
	lightRedButton = Button(screen, 450, 140, 120, "Light Red", lightBlue, black)
	redButton = Button(screen, 453, 185, 120, "", blue, black)
	redButton = Button(screen, 450, 180, 120, "Red", lightBlue, black)
	pinkButton = Button(screen, 593, 225, 120, "", blue, black)
	pinkButton = Button(screen, 590, 220, 120, "Pink", lightBlue, black)
	lightGreenButton = Button(screen, 593, 65, 120, "", blue, black)
	lightGreenButton = Button(screen, 590, 60, 120, "Light Green", lightBlue, black)
	greenButton = Button(screen, 593, 103, 120, "", blue, black)
	greenButton = Button(screen, 590, 100, 120, "Green", lightBlue, black)
	fuchsiaButton = Button(screen, 593, 145, 120, "", blue, black)
	fuchsiaButton = Button(screen, 590, 140, 120, "Fuchsia", lightBlue, black)
	blackButton = Button(screen, 593, 185, 120, "", blue, black)
	blackButton = Button(screen, 590, 180, 120, "Black", lightBlue, black)
	generateFigure = Button(screen, 453, 425, 225,"", blue, black)
	generateFigure = Button(screen, 450, 420, 225, "Look what you've done!", lightBlue, black)	
	while (eventsFlagII):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				 pygame.quit(); sys.exit();
			addEventII(event, yellowButton[0], yellowButton[1], text,screen)
			addEventII(event, blueButton[0], blueButton[1], text,screen)
			addEventII(event, darkBlueButton[0], darkBlueButton[1], text,screen)
			addEventII(event, lightBlueButton[0], lightBlueButton[1], text,screen)
			addEventII(event, purpleButton[0], purpleButton[1], text,screen)
			addEventII(event, orangeButton[0], orangeButton[1], text,screen)
			addEventII(event, lightRedButton[0], lightRedButton[1], text,screen)
			addEventII(event, redButton[0], redButton[1], text,screen)
			addEventII(event, pinkButton[0], pinkButton[1], text,screen)
			addEventII(event, lightGreenButton[0], lightGreenButton[1], text,screen)
			addEventII(event, greenButton[0], greenButton[1], text,screen)
			addEventII(event, blackButton[0], blackButton[1], text,screen)
			addEventII(event, fuchsiaButton[0], fuchsiaButton[1], text,screen)
			addEventII(event, generateFigure[0], generateFigure[1], text,screen)

# ==========================================================================
# Fractal atributes
# ==========================================================================

def selectfractalsAttributes(text):
	screen = window(749, 468)
	font=pygame.font.Font(None,30)
	secondaryText = font.render('Select color and size for the '+ text, True, darkBlue)
	screen.blit(secondaryText, (200,20))

	# Here should be the inputs or buttons to choose color and size.
	yellowButton = Button(screen, 313, 65, 120, "", blue, black)
	yellowButton = Button(screen, 310, 60, 120, "Yellow", lightBlue, black)
	blueButton = Button(screen, 313, 105, 120, "", blue, black)
	blueButton = Button(screen, 310, 100, 120, "Blue", lightBlue, black)
	darkBlueButton = Button(screen, 313, 145, 120, "", blue, black)
	darkBlueButton = Button(screen, 310, 140, 120, "Dark Blue", lightBlue, black)
	lightBlueButton = Button(screen, 313, 185, 120, " ", blue, black)
	lightBlueButton = Button(screen, 310, 180, 120, "Light Blue",lightBlue, black)
	purpleButton = Button(screen, 453, 65, 120, "", lightBlue, black)
	purpleButton = Button(screen, 450, 60, 120, "Purple", lightBlue, black)
	orangeButton = Button(screen, 453, 105, 120, "", blue, black)
	orangeButton = Button(screen, 450, 100, 120, "Orange", lightBlue, black)
	lightRedButton = Button(screen, 453, 145, 120, "", blue, black)
	lightRedButton = Button(screen, 450, 140, 120, "Light Red", lightBlue, black)
	redButton = Button(screen, 453, 185, 120, "", blue, black)
	redButton = Button(screen, 450, 180, 120, "Red", lightBlue, black)
	pinkButton = Button(screen, 593, 225, 120, "", blue, black)
	pinkButton = Button(screen, 590, 220, 120, "Pink", lightBlue, black)
	lightGreenButton = Button(screen, 593, 65, 120, "", blue, black)
	lightGreenButton = Button(screen, 590, 60, 120, "Light Green", lightBlue, black)
	greenButton = Button(screen, 593, 103, 120, "", blue, black)
	greenButton = Button(screen, 590, 100, 120, "Green", lightBlue, black)
	fuchsiaButton = Button(screen, 593, 145, 120, "", blue, black)
	fuchsiaButton = Button(screen, 590, 140, 120, "Fuchsia", lightBlue, black)
	blackButton = Button(screen, 593, 185, 120, "", blue, black)
	blackButton = Button(screen, 590, 180, 120, "Black", lightBlue, black)
	whiteButton = Button(screen, 453, 225, 120, "", blue, black)
	whiteButton = Button(screen, 450, 220, 120, "White", lightBlue, black)
	generateFigure = Button(screen, 453, 425, 225,"", blue, black)
	generateFigure = Button(screen, 450, 420, 225, "Look what you've done!", lightBlue, black)	
	while (eventsFlagII):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				 pygame.quit(); sys.exit();
			addeventIFractalattribute(event, yellowButton[0], yellowButton[1], text,screen)
			addeventIFractalattribute(event, blueButton[0], blueButton[1], text,screen)
			addeventIFractalattribute(event, darkBlueButton[0], darkBlueButton[1], text,screen)
			addeventIFractalattribute(event, lightBlueButton[0], lightBlueButton[1], text,screen)
			addeventIFractalattribute(event, purpleButton[0], purpleButton[1], text,screen)
			addeventIFractalattribute(event, orangeButton[0], orangeButton[1], text,screen)
			addeventIFractalattribute(event, lightRedButton[0], lightRedButton[1], text,screen)
			addeventIFractalattribute(event, redButton[0], redButton[1], text,screen)
			addeventIFractalattribute(event, pinkButton[0], pinkButton[1], text,screen)
			addeventIFractalattribute(event, lightGreenButton[0], lightGreenButton[1], text,screen)
			addeventIFractalattribute(event, greenButton[0], greenButton[1], text,screen)
			addeventIFractalattribute(event, blackButton[0], blackButton[1], text,screen)
			addeventIFractalattribute(event,whiteButton[0], whiteButton[1], text,screen)
			addeventIFractalattribute(event, fuchsiaButton[0], fuchsiaButton[1], text,screen)
			addeventIFractalattribute(event, generateFigure[0], generateFigure[1], text,screen)
# ==========================================================================
# Normal window functionality
# ==========================================================================
def selectNormals(text):
	screen = window(749, 468)
	font=pygame.font.Font(None,30)
	mainText = font.render('Select the figure to generate:', True, darkBlue)
	screen.blit(mainText, (320,20))
	squareButton = Button(screen, 323, 65, 150, '', blue, black)
	squareButton = Button(screen, 320, 60, 150, 'Square', lightBlue, black)
	rectangleButton = Button(screen, 323, 105, 150, '', blue, black)
	rectangleButton = Button(screen, 320, 100, 150, 'Rectangle', lightBlue, black) 
	triangleButton = Button(screen, 323, 145, 150, '', blue, black)
	triangleButton = Button(screen, 320, 140, 150, 'Triangle', lightBlue, black)
	circleButton = Button(screen, 323, 185, 150, '', blue, black)
	circleButton = Button(screen, 320, 180, 150, 'Circle', lightBlue, black)
	rhombusButton = Button(screen, 553, 65, 150, '', blue, black)
	rhombusButton = Button(screen, 550, 60, 150, 'Rhombus', lightBlue, black)
	hexagonButton = Button(screen, 553, 105, 150, '', blue, black)
	hexagonButton = Button(screen, 550, 100, 150, 'Hexagon', lightBlue, black)
	crazinessButton = Button(screen, 553, 145, 150, '',blue, black)
	crazinessButton = Button(screen, 550, 140, 150, 'Craziness', lightBlue, black)
	while (eventsFlagI):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				 pygame.quit(); sys.exit();
			addEventnormal(event, squareButton[0], squareButton[1]) 
			addEventnormal(event, rectangleButton[0], rectangleButton[1])
			addEventnormal(event, triangleButton[0], triangleButton[1])
			addEventnormal(event, circleButton[0], circleButton[1])
			addEventnormal(event, rhombusButton[0], rhombusButton[1])
			addEventnormal(event, hexagonButton[0], hexagonButton[1])
			addEventnormal(event, crazinessButton[0], crazinessButton[1])

# ==========================================================================
# fractals window functionality
# ==========================================================================
def selectFractals(text):
	screen = window(749, 468)
	font=pygame.font.Font(None,30)
	secondaryText = font.render('Select color and size for the '+ text, True, darkBlue)
	screen.blit(secondaryText, (310,20))
	squareFractal = Button(screen, 323, 65, 150, '', blue, black)
	squareFractal = Button(screen, 320, 60, 150, 'Square Fractal', lightBlue, black)
	koshFractal = Button(screen, 323, 145, 150, '', blue, black)
	koshFractal = Button(screen, 320, 140, 150, 'kosh Fractal', lightBlue, black)	
	Snowcone = Button(screen, 553, 65, 150, '', blue, black)
	Snowcone = Button(screen, 550, 60, 150, 'Snow cone', lightBlue, black)
	IFractal = Button(screen, 553, 105, 150, '', blue, black)
	IFractal = Button(screen, 550, 100, 150, 'IFractal', lightBlue, black)
	triangleFractal = Button(screen, 553, 145, 150, '', blue, black)
	triangleFractal = Button(screen, 550, 140, 150, 'Triangle Fractal', lightBlue, black)
	SierpinskiTriangle =Button(screen, 553, 185, 150, '', blue, black)
	SierpinskiTriangle = Button(screen, 550, 180, 150, 'Sierpinski', lightBlue, black)
	SierpinskiRug= Button (screen,323, 105,150, '', blue, black)
	SierpinskiRug= Button(screen, 320, 100, 150, 'Sierpinski Rug', lightBlue, black)
	while (eventsFlagI):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				 pygame.quit(); sys.exit();
			addEventFractal(event, squareFractal[0], squareFractal[1]) 
			
			addEventFractal(event, koshFractal[0], koshFractal[1])
			addEventFractal(event, triangleFractal[0], triangleFractal[1])
			addEventFractal(event, Snowcone [0], Snowcone[1])
			addEventFractal(event, IFractal[0], IFractal[1])
			addEventFractal(event, SierpinskiTriangle[0], SierpinskiTriangle[1])
			addEventFractal(event, SierpinskiRug[0], SierpinskiRug[1])
			
# ==========================================================================
# fractals window functionality input
# ==========================================================================
radius1=80
side1=150
def drawFigure(color, figure,radius,side):
	screen = window(749, 468)
	font=pygame.font.Font(None,30)
	secondaryTextI = font.render("Here is your figure!", True, darkBlue)
	screen.blit(secondaryTextI, (310,20))
	moreButton = Button(screen, 40, 40, 55, "+", blue, black)#button for make more bigger the shape	  
	lessButton = Button(screen, 40, 80, 55, "-", blue, black)#button for make less bigger the shape
	
	if figure == "Rectangle":
		rect=pygame.draw.rect(screen,color, (310,60,220,100))
	if figure == "Circle":
		circle=pygame.draw.circle(screen,color,(500,180),radius)
	if figure == 'Square':
		square=pygame.draw.rect(screen,color, (310,60,side,side))
	if figure == "Triangle":
		Triangle=pygame.draw.trigon(screen, color, ((450,50),(550,150),(350,150)))
	if figure == "Rhombus":
		Rhombus=pygame.draw.polygon(screen, color, ((450,50),(550,150),(450,250),(350,150)))
	if figure == "Hexagon":
		Hexagon= pygame.draw.polygon(screen, color, ((325,50),(475,50),(550,150),(475,250),(325,250),(250,150)))
	if figure == "Craziness":
		Craziness10=pygame.draw.rect(screen,color, (350,100,160,160))
		Craziness0=pygame.draw.circle(screen,color,(350,140),40)
		Craziness1=pygame.draw.circle(screen,color,(390,100),40)	 
		Craziness2=pygame.draw.rect(screen,black, (310,60,80,80))
		Craziness3=pygame.draw.circle(screen,white,(390,140),40)
		Craziness4=pygame.draw.circle(screen,color,(470,100),40)
		Craziness5=pygame.draw.circle(screen,color,(510,140),40)
		Craziness6=pygame.draw.rect(screen,black, (470,60,80,80))
		Craziness7=pygame.draw.circle(screen,white,(470,140),40)
		Craziness8=pygame.draw.circle(screen,color,(350,220),40)
		Craziness9=pygame.draw.circle(screen,color,(390,260),40)
		Craziness10=pygame.draw.rect(screen,black, (310,220,80,80))
		Craziness11=pygame.draw.circle(screen,white,(390,220),40)
		Craziness12=pygame.draw.circle(screen,color,(470,260),40)
		Craziness13=pygame.draw.circle(screen,color,(510,220),40)
		Craziness14=pygame.draw.rect(screen,black, (470,220,80,80))
		Craziness15=pygame.draw.circle(screen,white,(470,220),40)
		Craziness10=pygame.draw.rect(screen,white, (390,140,80,80))
		
	Backmain = Button(screen, 653, 425, 75,"", blue, black)	   
	Backmain = Button(screen, 650, 420, 75,"Back", lightBlue, black)
	SaveImagen = Button(screen, 378, 425, 75,"", blue, black)
	SaveImagen = Button(screen, 375, 420, 75,"Save", lightBlue, black)
	pygame.display.update()
	while(eventsFlagIII):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit(); sys.exit();
			addEventmain(event,Backmain[0],Backmain[1])
			addEventaddsize(event,moreButton[0],moreButton[1],figure,screen)
			addEventsize(event,lessButton[0],lessButton[1],figure,screen)
			addEventsave(event,SaveImagen[0],SaveImagen[1],screen)
# ==========================================================================
# Fractals draw functions
# ==========================================================================
def recursivekosh(count, xi,yi,xf,yf):
	if count==0:
		pygame.draw.line(screen,selectedColor,(xi,yi),(xf,yf),2)
	else:
			x1=xi+(xf-xi)/3.0
			y1=yi+(yf-yi)/3.0
			x3=xf-(xf-xi)/3.0
			y3=yf-(yf-yi)/3.0
			x2=(x1+x3)*math.cos(math.pi/3)+(y3-y1)*math.sin(math.pi/3)
			y2=(y1+y3)*math.cos(math.pi/3)-(x3-x1)*math.sin(math.pi/3)
			recursivekosh(count-1,xi,yi,x1,y1)
			recursivekosh(count-1,x1,y1,x2,y2)
			recursivekosh(count-1,x2,y2,x3,y3)
			recursivekosh(count-1,x3,y3,xf,yf)


def recursive_drawI(x, y, width, height, count):		
	
	
	#pygame.draw.line(screen,black,[x,y,width,height],1)
	pygame.draw.line(screen,
					 selectedColor,
					 [x + width*.25,height//2+y],
					 [x + width*.75,height//2+y],
					 2)
	pygame.draw.line(screen,
					 selectedColor,
					 [x+width*.25,(height*.5)//2+y],
					 [x+width*.25,(height*1.5)//2+y],
					 2)
	pygame.draw.line(screen,
					 selectedColor,
					 [x + width*.75,(height*.5)//2+y],
					 [x + width*.75,(height*1.5)//2+y],
					 2)
 
	if count > 1:
		count -= 1
		# Top left
		recursive_drawI(x, y,							width // 2, height // 2, count)
		# Top right
		recursive_drawI(x + width // 2, y,				width // 2, height // 2, count)
		# Bottom left
		recursive_drawI(x, y + width // 2,				width // 2, height // 2, count)
		# Bottom right
		recursive_drawI(x + width // 2, y + width // 2, width // 2, height // 2, count)
	 
def Recursivedrawsquare(x, y, width, height, count):
	pygame.draw.rect(screen,
					 selectedColor,
					 (x,y,width,height),2)
	
	if count > 1:
		count -= 1
		# Top left
		Recursivedrawsquare(x, y,							width // 2, height // 2, count)
		# Top right
		Recursivedrawsquare(x + width // 2, y,				width // 2, height // 2, count)
		# Bottom left
		Recursivedrawsquare(x, y + width // 2,				width // 2, height // 2, count)
		# Bottom right
		Recursivedrawsquare(x + width // 2, y + width // 2, width // 2, height // 2, count) 
 

def Recursivedrawtriangle(x, y, side, count):
   
	
	#pygame.draw.polygon(screen,color,point1(x,y),point2(x,y),point3(x,y),1)
	height=(((math.sqrt(3))/2)*side)
	pygame.draw.polygon(screen,
					 selectedColor,
					[(x,y),(x+side//2,y-height),(x+side,y)]
					,2)
	if count > 1:
		count -= 1
		# Top left
		Recursivedrawtriangle(x, y, side // 2, count)
		# Top right
		Recursivedrawtriangle(x + side / 2, y,side / 2, count)
		Recursivedrawtriangle(x+side/4 ,y-height/2,side/2,count)
		Recursivedrawtriangle(x+side-side/4,y-height/2,-side/2,count)
		
		
def recursivesnowcone(x, y, side, count):
	# Draw the rectangle
	
	#pygame.draw.polygon(screen,color,point1(x,y),point2(x,y),point3(x,y),1)
	height=(((math.sqrt(3))/2)*side)
	pygame.draw.polygon(screen,
					 selectedColor,
					[(x,y),(x+side//2,y-height),(x+side,y)]
					,3)
	if count > 1:
		count -= 1
		# Top left
		recursivesnowcone(x+side-side*2/3,y-height*2/3,-side/3, count)
		# Top right
		recursivesnowcone(x+side,y-height*2/3,-side/3, count)
		
		recursivesnowcone(x+side-side/3,y,-side/3,count)
def SierpinskiTriangle(x, y, side, count,width,selectedColor):
   
	
	#pygame.draw.polygon(screen,color,point1(x,y),point2(x,y),point3(x,y),1)
	side2=-side/2
	height=(((math.sqrt(3))/2)*side)
	height2=(((math.sqrt(3))/2)*side2)
	a=x+side-side/4
	b=y-height/2
	pygame.draw.polygon(screen,
					 black,
					[(x,y),(x+side/2,y-height),(x+side,y)]
					,0)
	pygame.draw.polygon(screen,
					 selectedColor,
					[(a,b),(a+side2/2,b-height2),(a+side2,b)]
					,0)
	
	if count > 1:
		count -= 1
		# Top left
		SierpinskiTriangle(x, y, side // 2, count,0,selectedColor)
		# Top right
		SierpinskiTriangle(x + side / 2, y,side / 2, count,0,selectedColor)
		
		SierpinskiTriangle(x+side/4 ,y-height/2,side/2,count,0,selectedColor)

def Seirpinskirug(x, y, width, height, count):
	pygame.draw.rect(screen,
					 black,
					 (x,y,width,height),0)
	width2=width/3
	height2=height/3
	a=x+width/3
	b=y+height/3
	pygame.draw.rect(screen,
					 selectedColor,
					 (a,b,width2,height2),0)
	
	if count > 1:
		count -= 1
		# Top left
		Seirpinskirug(x, y,							  width // 3, height // 3, count)
		# Top right
		Seirpinskirug(x + width // 3, y,			  width // 3, height // 3, count)
		# Bottom left
		Seirpinskirug(x, y + width // 3,			  width // 3, height // 3, count)
		# Bottom right
		Seirpinskirug(x + width // 3, y + 2*width // 3, width // 3, height // 3, count) 
		Seirpinskirug(x, y + 2*width // 3, width // 3, height // 3, count)
		Seirpinskirug(x + 2*width // 3, y + 2*width // 3, width // 3, height // 3, count)
		Seirpinskirug(x+2*width//3, y,							 width // 3, height // 3, count)
		Seirpinskirug(x+2*width//3, y + width // 3,							  width // 3, height // 3, count)
# ==========================================================================
# add event fractals
# ==========================================================================
def addeventIFractalattribute(event, rect, textButton, textFigure,screen):
	if event.type==pygame.MOUSEBUTTONDOWN:		  
		pos = pygame.mouse.get_pos()
		if rect.collidepoint(pos):
			global selectedColor,background
			if textButton != "Look what you've done!":
				if textButton == "Dark Blue":
					background = white
					selectedColor = darkBlue;
					darkBlueButton = Button(screen, 310, 140, 120, "Dark Blue", blue, black)
				elif textButton != "Dark Blue":
					darkBlueButton = Button(screen, 313, 145, 120, "",blue, black)
					darkBlueButton = Button(screen, 310, 140, 120, "Dark Blue",lightBlue, black)
					
				if textButton == "Blue":
					background = black
					selectedColor = blue;
					blueButton = Button(screen, 310, 100, 120, "Blue", blue, black)
				elif textButton != "Blue":
					blueButton = Button(screen, 313, 105, 120, "", blue, black)
					blueButton = Button(screen, 310, 100, 120, "Blue", lightBlue, black)
					
				if textButton == "Yellow":
					background = black
					selectedColor = yellow;
					yellowButton = Button(screen, 310, 60, 120, "Yellow", blue, black)
				elif textButton != "Yellow":				   
					yellowButton = Button(screen, 313, 65, 120, "", blue, black)
					yellowButton = Button(screen, 310, 60, 120, "Yellow", lightBlue, black)
					
				if textButton == "Purple":
					background =black
					selectedColor = purple;
					purpleButton = Button(screen, 450, 60, 120, "Purple", blue, black)
				elif textButton!="Purple":
					purpleButton = Button(screen, 453, 65, 120, "", blue, black)
					purpleButton = Button(screen, 450, 60, 120, "Purple", lightBlue, black)
					
				if textButton == "Light Blue":
					background = white
					selectedColor = lightBlue;
					lightBlueButton = Button(screen, 310, 180, 120, "Light Blue", blue, black)
				elif textButton !="Light Blue":
					lightBlueButton = Button(screen, 313, 185, 120, "", blue, black)
					lightBlueButton = Button(screen, 310, 180, 120, "Light Blue",lightBlue, black)
					
				if textButton == "Light Red":
					background = white
					selectedColor = lightRed;
					lightRedButton = Button(screen, 450, 140, 120, "Light Red", blue, black)
				elif textButton!="Light Red":
					lightRedButton = Button(screen, 453, 145, 120, "", blue, black)
					lightRedButton = Button(screen, 450, 140, 120, "Light Red", lightBlue, black)
					
				if textButton == "Orange":
					background = black
					selectedColor = orange;
					orangeButton = Button(screen, 450, 100, 120, "Orange", blue, black)
				elif textButton!="Orange":
					orangeButton = Button(screen, 453, 105, 120, "", blue, black)
					orangeButton = Button(screen, 450, 100, 120, "Orange", lightBlue, black)
					
				if textButton == "Red":
					background = black
					selectedColor = red ;
					redButton = Button(screen, 450, 180, 120, "Red", blue, black)
				elif textButton!="Red":
					redButton = Button(screen, 453, 185, 120, "",  blue, black)
					redButton = Button(screen, 450, 180, 120, "Red", lightBlue, black)
					
				if textButton == "Fuchsia":
					background = white
					selectedColor = fuchsia;
					fuchsiaButton = Button(screen, 590, 140, 120, "Fuchsia", blue, black)
				elif textButton !="Fuchsia":
					fuchsiaButton = Button(screen, 593, 145, 120, "", blue, black)
					fuchsiaButton = Button(screen, 590, 140, 120, "Fuchsia", lightBlue, black)
					
				if textButton == "Pink":
					background = black
					selectedColor = pink;
					pinkButton = Button(screen, 590, 220, 120, "Pink", blue, black)
				elif textButton !="Pink":
					pinkButton = Button(screen, 593, 225, 120, "", blue, black)
					pinkButton = Button(screen, 590, 220, 120, "Pink", lightBlue, black)
					
				if textButton == "Light Green":
					background = white
					selectedColor = lightGreen;
					lightGreenButton = Button(screen, 590, 60, 120, "Light Green", blue, black)
				elif textButton!="Light Green":
					lightGreenButton = Button(screen, 593, 65, 120, "", blue, black)
					lightGreenButton = Button(screen, 590, 60, 120, "Light Green", lightBlue, black)   
						 
				if textButton == "Green":
					background = white
					selectedColor = green;
					greenButton = Button(screen, 590, 100, 120, "Green", blue, black)
				elif textButton!= "Green":
					greenButton = Button(screen, 593, 105, 120, "", blue, black)
					greenButton = Button(screen, 590, 100, 120, "Green", lightBlue, black)		  
								
				if textButton == "Black":
					background = white
					selectedColor = black;
					blackButton = Button(screen, 590, 180, 120, "Black", blue, black)
				elif textButton!="Black":
					blackButton = Button(screen, 593, 185, 120, "", blue, black)
					blackButton = Button(screen, 590, 180, 120, "Black", lightBlue, black)
				if textButton == "White":
					background = white
					selectedColor = black;
					blackButton = Button(screen, 450, 220, 120, "White", blue, black)
				elif textButton!="White":
					blackButton = Button(screen, 453, 225, 120, "", blue, black)
					blackButton = Button(screen, 450, 220, 120, "White", lightBlue, black)
			else:
				drawfractal(selectedColor, textFigure,background)
				
				
				
def drawfractal(selectedColor, textFigure,background):
	global screen
	#size = [749, 468]
	#Iscreen = pygame.display.set_mode(size)
	screen = window(749, 468) 
	pygame.display.set_caption("Figure maker ADVANCED 2")	
# screen update speed
	screen.fill(background)
	backfractalButton= Button(screen, 50, 100, 120,"Back",blue,black)
	savefractalButton= Button(screen, 50, 200, 120, "save", blue, black)
	morefractalButton= Button(screen, 50, 300, 50, "+", blue, black)
	lessfractalButton= Button(screen, 50, 350, 50, "-", blue, black)		 

	
	x = 300
	y = 20
	if textFigure=="IFractal":
		recursive_drawI(x, y, 400, 400, fractal_level)
	if textFigure=="Square Fractal":
		Recursivedrawsquare(x, y, 400, 400, fractal_level)
	if textFigure=="Triangle Fractal":
		Recursivedrawtriangle(x,400,400,fractal_level)
	if textFigure=="kosh Fractal":
		recursivekosh(fractal_level,x,200,650,200)
	if textFigure=="Snow cone":
		recursivesnowcone(x,300,300,fractal_level)
	if textFigure=="Sierpinski":
		SierpinskiTriangle(x,400,400,fractal_level,0,selectedColor)
	if textFigure=="Sierpinski Rug":
		Seirpinskirug(x, y, 400, 400, fractal_level)	
	pygame.display.flip()
	
	while done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				pygame.quit();sys.exit();
			addEventmain(event,backfractalButton[0],backfractalButton[1])
			addEventaddsizefractal(event,morefractalButton[0],selectedColor,textFigure,background)
			addEventsizefractal(event,lessfractalButton[0],selectedColor,textFigure,background)
			addEventsave(event,savefractalButton[0],savefractalButton[1],screen)
	
	#clock.tick(1)										 # frames per second
# -------- Main Program Loop -----------


main()
