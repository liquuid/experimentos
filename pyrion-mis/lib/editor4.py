#!/usr/bin/env python
# -*- coding : utf8 -*-
import sys, pygame, random                                   # Importa os modulos do pygame
from cenario import *
from players import *
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


clock = pygame.time.Clock()
lista = [] 
cursor = Cursor(0, 0)
lista.append(cursor)
mousepos = ""
ktimer = 0
pygame.mouse.set_visible(0)
while 1:                   
	clock.tick(60)					     # Loop principal do game 
 
	for event in pygame.event.get():                     # Verifica eventos do teclado, mouse etc 
		if event.type == pygame.QUIT: sys.exit()     # Se o evento for do tipo QUIT encerra

	pressed_keys = pygame.key.get_pressed()
	#mousepos = pygame.mouse.get_pos()

	if pressed_keys[pygame.K_ESCAPE]:
		sys.exit()

	
	screen.fill(color)                                   # Preenche a tela com cor de fundo 
      

	for i in lista:
		
		if pygame.mouse.get_rel() != [0,0]:
                        i.rect.x = pygame.mouse.get_pos()[0]
                        i.rect.y = pygame.mouse.get_pos()[1]
                        
		cena(i,mapa,screen,[])


		if i.__class__ == Cursor:
                                        
				if pressed_keys[pygame.K_LEFT]:
					i.rect.x = i.rect.x - bloco
					pygame.mouse.set_pos([i.rect.x,i.rect.y])
				if pressed_keys[pygame.K_RIGHT]:
					i.rect.x = i.rect.x + bloco
					pygame.mouse.set_pos([i.rect.x,i.rect.y])
				if pressed_keys[pygame.K_UP]:
					i.rect.y = i.rect.y - bloco
					pygame.mouse.set_pos([i.rect.x,i.rect.y])
				if pressed_keys[pygame.K_DOWN]:
					i.rect.y = i.rect.y + bloco
					pygame.mouse.set_pos([i.rect.x,i.rect.y])
		
				if i.rect.x < 0:
					i.rect.x = width - bloco
				if i.rect.x > width - bloco:
					i.rect.x = 0
				if i.rect.y < 0:
					i.rect.y = height - bloco
				if i.rect.y > height - bloco: 
					i.rect.y = 0

				if pygame.mouse.get_pressed()[0]:
                                        mapa[i.rect.y/bloco][i.rect.x/bloco]=i.selec
                                
				if pygame.mouse.get_pressed()[2]:
                                        mapa[i.rect.y/bloco][i.rect.x/bloco]=0
			
				if pressed_keys[pygame.K_SPACE]:
					mapa[i.rect.y/bloco][i.rect.x/bloco] = i.selec
                                        
				if pressed_keys[pygame.K_DELETE]:
					mapa[i.rect.y/bloco][i.rect.x/bloco] = 0

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
				if pressed_keys[pygame.K_s]:
					arquivo = open('lib/fase.py','w')
					arquivo.write("mapa = [")
					for x in range(24):
						arquivo.write(str(mapa[x])+",\n")
					arquivo.write("]") 
					arquivo.close()
					print "salvo"
				if pressed_keys[pygame.K_l]:
					from fase import *

                        
                                					
		screen.blit(i.image,i.rect)
		
	pygame.display.flip()                                # Envia o que foi desenhado para o monitor 










