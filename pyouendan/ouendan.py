import pygame
import sys,os
screen_size = width , heigth = 800 ,600
screen = pygame.display.set_mode(screen_size)

pygame.init()

class Button(pygame.sprite.Sprite):
	def __init__(self,numero,posX,posY,showTime,lifeTime,color):
		self.circ = 300
		self.num = numero
		self.x = posX
		self.y = posY
		self.lt = lifeTime
		self.cl = color
		self.st = showTime

	def draw(self):
		pygame.draw.circle(screen,(255,0,100),(self.x,self.y),50,0)
		screen.blit(pygame.font.SysFont("arial", 60).render(self.num,False,(200,200,200)),(self.x-20,self.y-30))
		pygame.draw.circle(screen,(0,0,255),(self.x,self.y),self.circ,1)
		
def main():
	curTime = 0
	f = open("discipline.data","r")
	f = f.read()
	li = []
	lista_obj = []
	for i in f.split():
		li.append(i)
	
	for i in li:
		i = i.split(",")
		lista_obj.append(Button(str(i[0]),int(i[1]),int(i[2]),int(i[3]),int(i[4]),int(i[5])))

	while 1:
		
		for obj in lista_obj:
			if obj.st < curTime:
				if obj.circ > 50:
					obj.circ = obj.circ - 300/obj.lt
					obj.draw()


		font = pygame.font.SysFont("arial", 32)
		text = font.render(str(curTime)+"::Ouendan!!!",False,(200,200,255))
		screen.blit(text,(500,30))
		pygame.display.flip()
		screen.fill((0, 0, 0))
		curTime = curTime + 1




if __name__ == '__main__':
	main()

