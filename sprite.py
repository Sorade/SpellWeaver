# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 18:27:51 2016

@author: Julien
"""
import pygame
import functions as fn

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        self.img_ref = 'square'
        self.rect = pygame.Rect(50,50,50,50)
        self.center = (0,0)
        self.blit_pos = self.center
        self.speed = 120 #px/s
        self.dest = (250,250)
        self.obstacles = []
        self.enemies = []
        self.allies = []
        
    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, center):
        self.blit_pos = fn.sum_tulp(center,(-25,-25))
        self.rect.center = center
        self._center = center
        
    def check_collision(self,new_pos, group): #could use spritecollideany for groups
        rect = self.rect
        '''check x-axis collision'''
        rect.center = (new_pos[0],self.center[1])
        xcol = rect.collidelist(group)
        '''check y-axis collision'''
        rect.center = (self.center[0],new_pos[1])
        ycol = rect.collidelist(group)
        return xcol,ycol
