import pygame, math , random
class Game(pygame.sprite.Sprite):
        def __init__(self,level,n_souls):
                self.score = 0
                self.level = level
                self.n_souls = 1

