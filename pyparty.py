import sys
import pygame,math,cmath
from pygame.locals import *
flag=True

def Windons():
  pygame.init()
  screen = pygame.display.set_mode((1024,600))
  background = pygame.image.load("background.jpg").convert()
  pygame.display.set_caption("PyPARTY")
  screen.blit(background,(0,0))
  pygame.display.update()
  return screen
  while (flag):
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();
Windons()
while (eventsFlagI):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				 pygame.quit(); sys.exit();
