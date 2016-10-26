# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:51:15 2016

@author: Julien
"""

import pygame
from pygame.locals import*
import random
import sys
import functions as fn
import variables as v
import characters as ch
import data


class Level():
    def __init__(self,game):
        self.game = game
        self.player = ch.Human((100,100),'human')
        self.enemy = ch.Orc((250,250))
        black_bg = pygame.Surface((800,600))
        black_bg.fill((200,200,200))
        black_bg.set_alpha(100)
        self.bg = black_bg
        
        self.all_sprites = pygame.sprite.Group(self.player,self.enemy)
        self.all_characters = pygame.sprite.Group(self.player,self.enemy)

        self.assign_obstacles()
        self.assign_enemies()
        
        self.casts = pygame.sprite.Group()
        self.to_blit = pygame.sprite.Group(self.player,self.enemy)
        
    def assign_obstacles(self):
        for s in self.all_sprites:
            [s.obstacles.add(ss) for ss in self.all_sprites if ss != s]
            
    def assign_enemies(self):
        for s in self.all_characters:
            [s.enemies.add(ss) for ss in self.all_characters if ss.cat in s.enemy_cats]
        
