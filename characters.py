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
        self.speed = 120 #px/s
        self.type = AI_type # cpu or human
        self.dest = (250,250)
        self.obstacles = []
        self.enemies = []
        self.allies = []
        self.dead = False
#        self.casts = {'LMB' : CAC, 
#                      'RMB' : Spell, 
#                      '1' : Res}
        

                      
    '''AI Logic'''
#    def act(self):
#        if enemies whithin radius and hp > 150:
#            self.move_to(enemy.center)
#        if enemies collide and hp > 150:
#            self.cast('LMB', enemy_in_range.center)
#        else:
#            self.move_to(random_pos)
            
        
    '''Movement Logic'''
    def set_dest(self, dest = None):
        if self.type == 'human':
            self.dest = pygame.mouse.get_pos()
        else:
                self.dest = dest
                    
    def move_to(self):
        if self.dest != self.center:
            dist = fn.dist(self.center,self.dest)
            mvt_ratio = (self.speed/v.FPS)/dist if v.FPS != 0 else 0
            dx,dy = self.dest[0] - self.center[0] ,self.dest[1] - self.center[1]
            mx, my = dx * mvt_ratio,dy * mvt_ratio
            move_by = (mx, my)
            new_pos = fn.sum_tulp(self.center,move_by)
            new_pos = (int(round(new_pos[0])),int(round(new_pos[1])))
            xcol,ycol = self.check_collision(new_pos,self.obstacles)
            if xcol == -1 and ycol == -1: 
                self.center = new_pos
            elif xcol != -1 and ycol == -1:
                self.center = (self.center[0],new_pos[1])
            elif xcol == -1 and ycol != -1:
                self.center = (new_pos[0],self.center[1])
            #self.center = new_pos
    
    '''Combat Logic'''

    def cast(self,current_clicked, pos):
        #cast = self.casts[current_clicked](self, pos)
        cast = c.Spell(self)
        v.current_lvl.casts.add(cast)
        
    def receive_dmg(self,dmg):
        self.hp += dmg
        if self.hp <= 0:
            self.dead = True
        else:
            self.dead = False
