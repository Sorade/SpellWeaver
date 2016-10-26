# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 18:27:51 2016

@author: Julien
"""
import pygame
import functions as fn
import variables as v
import data

class MySprite(pygame.sprite.Sprite):
    def __init__(self, img_ref, center, speed, callout = []):
        super(MySprite, self).__init__()
        self.blit_pos = None
        self.rect = data.images[img_ref].get_rect() #temp
        self.center = center
        self.img_ref = img_ref
        self.speed = speed #px/s
        self.dest = (250,250)
        self.obstacles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.allies = []
        self.callouts = callout
        self.callouts_save = None
        self.received_callouts = None
        
    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, center):
        self.rect.center = center
        self.blit_pos = (self.rect.x, self.rect.y)#fn.sum_tulp(center,(-self.rect.w/2,-self.rect.h/2))
        self._center = center
        
    @property
    def img_ref(self):
        return self._img_ref

    @img_ref.setter
    def img_ref(self, img_ref):
        self.rect = data.images[img_ref].get_rect()
        self.rect.center = self.center
        self.blit_pos = (self.rect.x, self.rect.y)
        self._img_ref = img_ref
        
    def add_callout(self, callout):
        if callout not in self.callouts: self.callouts.append(callout)
            
    def add_save_callout(self, callout):
        if callout not in self.callouts_save: self.callouts_save.append(callout)
            
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
            mvt_ratio = (self.speed/(v.FPS))/dist if v.FPS != 0 else 0
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
            
            '''fixes dest if nearby'''
            if pygame.Rect(self.center,(6,6)).collidepoint(self.dest):
                self.center = self.dest
                
    def listen(self,group, collision_ratio): #listens to callouts from sprites in a group
        self.callouts_save = list(self.callouts)
        colliding_sprites = self.check_collision_with_group(group, collided = pygame.sprite.collide_rect_ratio(collision_ratio))
        colliding_sprites.remove(self)
        colliding_sprites = [x for x in colliding_sprites if fn.overlap(self.col_ls,x.col_ls)]
        self.received_callouts = [call for s in colliding_sprites for call in s.callouts]
    
    def callout(self):
        pass

    def check_collision_with_group(self,group, collided = None):
        return pygame.sprite.spritecollide(self,group, False, collided = collided)

  