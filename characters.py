# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:50:01 2016

@author: Julien
"""

import pygame
import variables as v
import functions as fn
import random
from sprite import MySprite
import casts as c
        
        
class Character(MySprite):
    def __init__(self, (x,y), AI_type = 'cpu'):
        super(Character, self).__init__()
        self.hp = 500
        self.img_ref = 'square'
        self.rect = pygame.Rect(50,50,50,50)
        self.center = (x,y)
        self.blit_pos = self.center
        self.speed = 100 #px/s
        self.type = AI_type # cpu or human
        self.dest = (250,250)
        self.cat = 'generic'
        self.enemy_cats = ['generic']
        self.dead = False
        self.casts = {'LMB' : c.FireBall, 
                      'RMB' : c.Regen, 
                      '1' : None}
        

                      
    '''AI Logic'''
#    def act(self):
#        if enemies whithin radius and hp > 150:
#            self.move_to(enemy.center)
#        if enemies collide and hp > 150:
#            self.cast('LMB', enemy_in_range.center)
#        else:
#            self.move_to(random_pos)
            
        
    
    '''Combat Logic'''

    def cast(self,current_clicked, pos):
        if self.casts[current_clicked] is not None:
            cast = self.casts[current_clicked](self)
            v.current_lvl.casts.add(cast)
            v.current_lvl.all_sprites.add(cast)
        
    def receive_dmg(self,dmg):
        self.hp += dmg
        if self.hp <= 0:
            self.dead = True
        else:
            self.dead = False
            
class Orc(Character):
    def __init__(self, (x,y), AI_type = 'cpu'):
        super(Orc, self).__init__((x,y))
        self.hp = 500
        self.img_ref = 'orc'
        self.rect = pygame.Rect(50,50,50,50)
        self.center = (x,y)
        self.blit_pos = self.center
        self.speed = 120 #px/s
        self.type = AI_type # cpu or human
        self.dest = (250,250)
        self.cat = 'orc'
        self.enemy_cats = ['human']
        self.allies = []
        self.dead = False
        self.casts = {'LMB' : None, 
                      'RMB' : c.FireBall, 
                      '1' : None}
                      
class Human(Character):
    def __init__(self, (x,y), AI_type = 'cpu'):
        super(Human, self).__init__((x,y))
        self.hp = 500
        self.img_ref = 'human'
        self.rect = pygame.Rect(50,50,50,50)
        self.center = (x,y)
        self.blit_pos = self.center
        self.speed = 120 #px/s
        self.type = AI_type # cpu or human
        self.dest = (250,250)
        self.cat = 'human'
        self.enemy_cats = ['orc']
        self.allies = []
        self.dead = False
        self.casts = {'LMB' : None, 
                      'RMB' : c.FireBall, 
                      'MMB' : c.WaterJet}
    