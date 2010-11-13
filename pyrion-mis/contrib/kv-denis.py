#!/usr/bin/env python
# -*- coding : utf8 -*-
import sys, pygame, random                                   # Importa os modulos do pygame
from fase import *

print mapa

pygame.init()                                                # Inicializa esses modulos

size = width, height = 640, 480

color = 0, 0, 0                                        # Define a cor de fundo da tela
screen = pygame.display.set_mode(size)                       # Inicializa a janela onde rola o game 

bloco = 20 

pygame.mixer.init()
click = pygame.mixer.Sound("jump.wav")

clock = pygame.time.Clock()
lista = [] 
ktimer = 0

class Player(pygame.sprite.Sprite):
		def __init__(self,player_x,player_y):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.transform.scale2x(pygame.image.load("mario1.png"))
			self.rect  = self.image.get_rect()
			self.rect.x = player_x
			self.rect.y = player_y
			self.player = 1
			self.isalive = 0
			self.item = 0
			
class Soul(pygame.sprite.Sprite):
		def __init__(self,soul_x,soul_y):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load("bola.png")
			self.rect  = self.image.get_rect()
			self.rect.x = soul_x
			self.rect.y = soul_y
			self.soul = 1
			self.visivel = 1

class Game(pygame.sprite.Sprite):
		def __init__(self,level):
			self.score = 0
			self.level  = level
			self.n_souls = 1
			
lista.append(Player(0,0))

while 1:                   
	clock.tick(60)					     # Loop principal do game 


	for event in pygame.event.get():                     # Verifica eventos do teclado, mouse etc 
		if event.type == pygame.QUIT: sys.exit()     # Se o evento for do tipo QUIT encerra

	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[pygame.K_ESCAPE]:
		sys.exit()

	screen.fill(color)                                   # Preenche a tela com cor de fundo 


	font = pygame.font.Font(None,36)
	text = font.render("Kings Valley Py",2,(200,100,50))
	#textpos = text.get_rect(0,0)



	for i in lista:
		print lista
		for y in range(24):
			for x in range(32):
				if mapa[y][x] == 1:
					screen.blit(pygame.image.load("terra.gif"),[x*20, y*20])
				if mapa[y][x] == 2:
					screen.blit(pygame.image.load("pedra.jpg"),[x*20, y*20])
				if mapa[y][x] == 3:
					screen.blit(pygame.image.load("bola.png"),[x*20, y*20])
				if mapa[y][x] == 4:
					screen.blit(pygame.image.load("britadeira.jpg"),[x*20, y*20])
				if mapa[y][x] == 5:
					screen.blit(pygame.image.load("caixao.gif"),[x*20, y*20])
				
				if mapa[y][x] == 6:
					if not i.isalive:
						screen.blit(i.image,[y*20,x*20])
						i.rect = [y*20,x*20]
						isalive = 1
					
				if mapa[y][x] == 7:
					screen.blit(pygame.image.load("pa.png"),[x*20, y*20])
				if mapa[y][x] == 8:
					screen.blit(pygame.image.load("portafechada.jpg"),[x*20, y*20])
					
		if i.player and i.isalive:
			if pressed_keys[pygame.K_LEFT]:
				i.rect.x = i.rect.x - 5
			if pressed_keys[pygame.K_RIGHT]:
				i.rect.x = i.rect.x + 5
			if pressed_keys[pygame.K_UP]:
				i.rect.y = i.rect.y - 5
			if pressed_keys[pygame.K_DOWN]:
				i.rect.y = i.rect.y + 5
			if pressed_keys[pygame.K_SPACE]:
				pass
			
		screen.blit(i.image,i.rect)	
		
	screen.blit(text,[0,0])
	pygame.display.flip()                                # Envia o que foi desenhado para o monitor 
