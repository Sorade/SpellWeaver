# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 18:27:51 2016

@author: Julien
"""
import pygame
import functions as fn
import variables as v

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        self.img_ref = 'square'
        self.rect = pygame.Rect(50,50,50,50)
        self.center = (0,0)
        self.blit_pos = self.center
        self.speed = 120 #px/s
        self.dest = (250,250)
        self.obstacles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
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
        xcol = pygame.sprite.spritecollide(self,group, False)
        '''check y-axis collision'''
        rect.center = (self.center[0],new_pos[1])
        ycol = pygame.sprite.spritecollide(self,group, False)

        return xcol,ycol
        
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
            if xcol == [] and ycol == []: 
                self.center = new_pos
            elif xcol != [] and ycol == []:
                self.center = (self.center[0],new_pos[1])
            elif xcol == [] and ycol != []:
                self.center = (new_pos[0],self.center[1])
            #self.center = new_pos