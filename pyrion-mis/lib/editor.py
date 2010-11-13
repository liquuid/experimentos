#!/usr/bin/env python
# -*- coding : utf8 -*-
import sys, pygame, random                                   # Importa os modulos do pygame
pygame.init()                                                # Inicializa esses modulos

size = width, height = 600, 400

color = 255, 255, 255                                        # Define a cor de fundo da tela
screen = pygame.display.set_mode(size)                       # Inicializa a janela onde rola o game 

pygame.mixer.init()
click = pygame.mixer.Sound("data/jump.wav")

class Cursor(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("data/bola.png")
		self.rect  = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.cursor = 1

class Chao(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("data/bolar.png")
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
		if i.cursor:
			if ktimer > 5:
				if pressed_keys[pygame.K_LEFT]:
					i.rect.x = i.rect.x - 50
				if pressed_keys[pygame.K_RIGHT]:
					i.rect.x = i.rect.x + 50
				if pressed_keys[pygame.K_UP]:
					i.rect.y = i.rect.y - 50		
				if pressed_keys[pygame.K_DOWN]:
					i.rect.y = i.rect.y + 50
				ktimer = 0
		
		
				if i.rect.x < 0:
					i.rect.x = width - 50
				if i.rect.x > width:
					i.rect.x = 0
				if i.rect.y < 0:
					i.rect.y = height - 50
				if i.rect.y > height: 
					i.rect.y = 0
			
				if pressed_keys[pygame.K_SPACE]:
					lista.insert(0,Chao(i.rect.x,i.rect.y))
					print lista
					click.play()
			
		
		screen.blit(i.image,i.rect)
	
	ktimer = ktimer + 1
	pygame.display.flip()                                # Envia o que foi desenhado para o monitor 










