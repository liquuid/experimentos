import pygame
import sys,os
import discipline
screen_size = width , heigth = 800 ,600
screen = pygame.display.set_mode(screen_size)

pygame.init()

		
def main():
	curTime = 0
	f = open("discipline.data","r")
	f = f.read()
	li = []
	lista_obj = []

	while 1:
		
		font = pygame.font.SysFont("arial", 32)
		text = font.render(str(curTime)+"::Ouendan!!!",False,(200,200,255))
		screen.blit(text,(500,30))
		pygame.display.flip()
		screen.fill((0, 0, 0))
		curTime = curTime + 1




if __name__ == '__main__':
	main()

