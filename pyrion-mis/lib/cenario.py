import pygame, math, random
#from fase import *
#from main import mapa
from players import *

class Terra(pygame.sprite.Sprite):
        def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("data/terra.gif")
                self.rect  = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

class Pedra(pygame.sprite.Sprite):
        def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("data/pedra.jpg")
                self.rect  = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

class Britadeira(pygame.sprite.Sprite):
        def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("data/britadeira.jpg")
                self.rect  = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

class Caixao(pygame.sprite.Sprite):
        def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("data/caixao.gif")
                self.rect  = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

class Pa(pygame.sprite.Sprite):
        def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("data/pa.png")
                self.rect  = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

class Porta(pygame.sprite.Sprite):
        def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self)
                self.image_fechada = pygame.image.load("data/portafechada.jpg")
		self.image_aberta = pygame.image.load("data/portaaberta.jpg")
		self.image = image_fechada
                self.rect  = self.image.get_rect()
		self.aberta = 0 
                self.rect.x = x
                self.rect.y = y



def cena(i,mapa,screen,lista):
	for y in range(24):
		for x in range(32):
			if mapa[y][x] == 1:
				if lista:
					lista.append(Terra(x*20,y*20))
				else:
					screen.blit(pygame.image.load("data/terra.gif"),[x*20, y*20])
			if mapa[y][x] == 2:
				if lista:
					lista.append(Pedra(x*20,y*20))
				else:
					screen.blit(pygame.image.load("data/pedra.jpg"),[x*20, y*20])
			if mapa[y][x] == 3:
				if lista:
					lista.append(Soul(x*20,y*20))
				else:
					screen.blit(pygame.image.load("data/bola.png"),[x*20, y*20])

			if mapa[y][x] == 4:
				if lista:
					lista.append(Britadeira(x*20,y*20))
				else:
					screen.blit(pygame.image.load("data/britadeira.jpg"),[x*20, y*20])

			if mapa[y][x] == 5:
				if lista:
					lista.append(Caixao(x*20,y*20))
				else:
					screen.blit(pygame.image.load("data/caixao.gif"),[x*20, y*20])


			if mapa[y][x] == 6:
				
				if i.__class__ == Player:
					if not i.isalive:
						screen.blit(i.image,[y*20 ,x*20 ] )
						i.rect.y = y*20 
						i.rect.x = x*20
						i.isalive = 1

				if i.__class__ == Cursor:
					screen.blit(pygame.image.load("data/mario1.png"),[x*20, y*20])

			if mapa[y][x] == 7:
				if lista:
					lista.append(Pa(x*20,y*20))
				else:
					screen.blit(pygame.image.load("data/pa.jpg"),[x*20, y*20])

			if mapa[y][x] == 8:
				if lista:
					lista.append(Porta(x*20,y*20))
				else:
					screen.blit(pygame.image.load("data/portafechada.jpg"),[x*20, y*20])



