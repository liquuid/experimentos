#!/usr/bin/env python
# -*- coding : utf8 -*-
import sys, pygame, random                                   # Importa os modulos do pygame
pygame.init()                                                # Inicializa esses modulos

size = width, height = 640, 480

color = 0, 0, 0                                        # Define a cor de fundo da tela
screen = pygame.display.set_mode(size)                       # Inicializa a janela onde rola o game 

bloco = 20 
 
mapa = []
	
for i in range(24):
	mapa.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])


pygame.mixer.init()
click = pygame.mixer.Sound("data/jump.wav")

class Cursor(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("data/cursor.png")
		self.rect  = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.selec = 1
		self.cursor = 1

class Chao(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("data/terra.gif")
		self.rect  = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.visivel = 1
		self.cursor = 0
	
	def remover(self,x,y):
		self.visivel = 0
		



clock = pygame.time.Clock()
lista = [] 
cursor = Cursor(0, 0)
lista.append(cursor)

ktimer = 0
while 1:                   
	clock.tick(60)					     # Loop principal do game 


	for event in pygame.event.get():                     # Verifica eventos do teclado, mouse etc 
		if event.type == pygame.QUIT: sys.exit()     # Se o evento for do tipo QUIT encerra

	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[pygame.K_ESCAPE]:
		sys.exit()

	
	screen.fill(color)                                   # Preenche a tela com cor de fundo 
      

	for i in lista:

		for y in range(24):
			for x in range(32):
				if mapa[y][x] == 1:
					screen.blit(pygame.image.load("data/terra.gif"),[x*20, y*20])
				if mapa[y][x] == 2:
					screen.blit(pygame.image.load("data/pedra.jpg"),[x*20, y*20])
				if mapa[y][x] == 3:
					screen.blit(pygame.image.load("data/bola.png"),[x*20, y*20])
				if mapa[y][x] == 4:
					screen.blit(pygame.image.load("data/britadeira.jpg"),[x*20, y*20])
				if mapa[y][x] == 5:
					screen.blit(pygame.image.load("data/caixao.gif"),[x*20, y*20])
				if mapa[y][x] == 6:
					screen.blit(pygame.image.load("data/mario1.png"),[x*20, y*20])
				if mapa[y][x] == 7:
					screen.blit(pygame.image.load("data/pa.png"),[x*20, y*20])
				if mapa[y][x] == 8:
					screen.blit(pygame.image.load("data/portafechada.jpg"),[x*20, y*20])
					
		if i.cursor:
			if ktimer > 5:
				if pressed_keys[pygame.K_LEFT]:
					i.rect.x = i.rect.x - bloco
					#print i.rect.x , i.rect.y , i.rect.x/bloco , i.rect.y/bloco
				if pressed_keys[pygame.K_RIGHT]:
					i.rect.x = i.rect.x + bloco
					#print i.rect.x, i.rect.y , i.rect.x/bloco , i.rect.y/bloco
				if pressed_keys[pygame.K_UP]:
					i.rect.y = i.rect.y - bloco
					#print i.rect.x, i.rect.y , i.rect.x/bloco , i.rect.y/bloco
				if pressed_keys[pygame.K_DOWN]:
					i.rect.y = i.rect.y + bloco
					#print i.rect.x, i.rect.y , i.rect.x/bloco , i.rect.y/bloco
				ktimer = 0
		
		
				if i.rect.x < 0:
					i.rect.x = width - bloco
				if i.rect.x > width - bloco:
					i.rect.x = 0
				if i.rect.y < 0:
					i.rect.y = height - bloco
				if i.rect.y > height - bloco: 
					i.rect.y = 0
			
				if pressed_keys[pygame.K_SPACE]:
		#			lista.insert(0,Chao(i.rect.x,i.rect.y))
					
					if mapa[i.rect.y/bloco][i.rect.x/bloco] == i.selec:
						mapa[i.rect.y/bloco][i.rect.x/bloco] = 0
					else:
						mapa[i.rect.y/bloco][i.rect.x/bloco] = i.selec
					
					print i.rect.x, i.rect.y , i.rect.x/bloco , i.rect.y/bloco
		#			print lista
		#			click.play()
				if pressed_keys[pygame.K_0]:
					i.selec = 0
				if pressed_keys[pygame.K_1]:
					i.selec = 1
				if pressed_keys[pygame.K_2]:
					i.selec = 2
				if pressed_keys[pygame.K_3]:
					i.selec = 3
				if pressed_keys[pygame.K_4]:
					i.selec = 4
				if pressed_keys[pygame.K_5]:
					i.selec = 5
				if pressed_keys[pygame.K_6]:
					i.selec = 6
				if pressed_keys[pygame.K_7]:
					i.selec = 7
				if pressed_keys[pygame.K_8]:
					i.selec = 8
					
		
			screen.blit(i.image,i.rect)
					
			
		
	ktimer = ktimer + 1
	pygame.display.flip()                                # Envia o que foi desenhado para o monitor 










