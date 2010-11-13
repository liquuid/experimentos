#!/usr/bin/env python
# -*- coding : utf8 -*-
import sys, pygame, random                                   # Importa os modulos do pygame
from fase import *
from players import *
from game import *
from cenario import *

pygame.init()                                                # Inicializa esses modulos
pygame.mixer.init()

bgm = pygame.mixer.Sound("data/bgm.ogg")
#bgm.play(-1)

size = width, height = 640, 480
color = 0, 0, 0                                        # Define a cor de fundo da tela
screen = pygame.display.set_mode(size)                       # Inicializa a janela onde rola o game 
bloco = 20 
click = pygame.mixer.Sound("data/jump.wav")
clock = pygame.time.Clock()


lista = []
lista.append(Player(0,0))
cena(lista[0],mapa,screen,lista)
while 1:                   
	clock.tick(60)					     # Loop principal do game 

	for event in pygame.event.get():                     # Verifica eventos do teclado, mouse etc 
		if event.type == pygame.QUIT: sys.exit()     # Se o evento for do tipo QUIT encerra

	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[pygame.K_ESCAPE]:
		sys.exit()

	screen.fill(color)                                   # Preenche a tela com cor de fundo 

	font = pygame.font.Font(None,20)
	text = font.render("Kings Valley Sux",10,(200,220,25))


	for i in lista:
		if (i.__class__ == Player)  and i.isalive:
			if pressed_keys[pygame.K_LEFT]:
				i.rect.x = i.rect.x - 3
				i.direc = 0
				i.image=i.image_e
			if pressed_keys[pygame.K_RIGHT]:
				i.rect.x = i.rect.x + 3
				i.direc = 1
				i.image=i.image_d
			if pressed_keys[pygame.K_UP]:
				i.rect.y = i.rect.y - 3
				i.jump()
			if pressed_keys[pygame.K_DOWN]:
				i.rect.y = i.rect.y + 3
			if pressed_keys[pygame.K_SPACE]:
				pass

		if i.rect.colliderect(lista[0]) and not (i.__class__ == Player) :
			if  ((i.__class__ == Pedra) or (i.__class__ == Terra)):
				lista[0].rect.bottom = i.rect.top
				i.acely =0
		if (i.__class__ == Player) :
			if i.jumping:
				i.jumping = i.jumping + 1
			if i.jumping > 0 and i.jumping <=6 :
				i.rect.y = i.rect.y - 6
			else:
				i.jumping = 0
				

			lista[0].rect.y=lista[0].rect.y + 3
		
		screen.blit(i.image,i.rect)

		



	screen.blit(text,[0,0])
	pygame.display.flip()                                # Envia o que foi desenhado para o monitor 
