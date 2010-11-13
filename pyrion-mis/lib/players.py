import pygame, math , random

class Player(pygame.sprite.Sprite):
        def __init__(self,player_x,player_y):
                pygame.sprite.Sprite.__init__(self)
                self.image_d=pygame.image.load("data/mario1.png")
		self.image_e=pygame.transform.flip(self.image_d,1,0)
		self.image=pygame.image.load("data/mario1.png")
		self.rect = self.image.get_rect()
                self.rect.x = player_x
                self.rect.y = player_y
                self.direc = 1
		self.isalive = 0
                self.item = 0
		self.acely = 0
		self.jumping = 0

        def jump(self):
		jump = pygame.mixer.Sound("data/jump.wav")
                jump.play()
                self.image = pygame.image.load("data/mario6.png")
                if self.direc == 0:
                  self.image = self.image
                else:
                  self.image=pygame.transform.flip(self.image,1,0)
		self.jumping = 1

        def die(self):
		self.isalive = 0
		pass

        def respawn(self):
                self.rect.x = 50
                self.rect.y = 400
                self.isalive = 1

	

class Soul(pygame.sprite.Sprite):
        def __init__(self,pos_x,pos_y):
                pygame.sprite.Sprite.__init__(self)
                self.image=pygame.image.load("data/bola.png")
                self.rect = self.image.get_rect()
                self.rect.x = pos_x
                self.rect.y = pos_y
                self.visivel = 1

class Cursor(pygame.sprite.Sprite):
        def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("data/cursor.png")
                self.rect  = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.selec = 1

