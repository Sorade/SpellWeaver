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
    def __init__(self, img_ref, center, speed, hp, cat, enemy_cats, AI_type = 'cpu'):
        super(Character, self).__init__(img_ref, center, speed)
        self.hp = hp
        self.type = AI_type # cpu or human
        self.cat = cat
        self.enemy_cats = enemy_cats
        self.dead = False
        self.casts = {'LMB' : c.FireBall, 
                      'RMB' : c.Regen, 
                      '1' : None}
        
    def update(self):
        self.move_to()

                      
    '''AI Logic'''
#    def act(self):
#        if enemies whithin radius and hp > 150:
#            self.move_to(enemy.center)
#        if enemies collide and hp > 150:
#            self.cast('LMB', enemy_in_range.center)
#        else:
#            self.move_to(random_pos)
            
        
    
    '''Combat Logic'''

    def cast(self,current_clicked):
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
    def __init__(self, center):
        super(Orc, self).__init__('orc', center, 120, 500, 'orc', ['human'])
        self.casts = {'LMB' : None, 
                      'RMB' : c.FireBall, 
                      '1' : None}
                      
class Human(Character):
    def __init__(self, center, AI_type = 'human'):
        super(Human, self).__init__('human', center, 120, 500, 'human', ['orc'], AI_type)
        self.casts = {'LMB' : None, 
                      'RMB' : c.FireBall, 
                      'MMB' : c.WaterJet,
                      't' : c.MakeTree}
    