# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:49:52 2016

@author: Julien
"""
import pygame
import variables as v
from sprite import MySprite
import functions as fn



class Cast(MySprite):
    def __init__(self, initiator,  duration):
        super(Cast, self).__init__()
        self.initiator = initiator
        self.targets = initiator.enemies
        self.duration = duration
        self.col_ls = None
        self.attributes = ['flammable','freezable','conductive','fertile']
        self.states = {'ablaze' : False,  
                       'frozen' : False, 
                       'electrified' : False,
                       'blooming': False}
                       
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if duration <= 0:
            self.kill()
        self._duration = duration
                       

    def execute(self):
        pass
    
    
    def check_states(self):
        pass

    
    def check_blit(self):
        if self.duration > 0:
            v.current_lvl.to_blit.add(self) 
        else:
            v.current_lvl.to_blit.remove(self)
            
   
class Regen(Cast):
    def __init__(self, initiator):
        super(Regen, self).__init__(initiator, 10*v.FPS)
        self.targets = initiator.allies
        self.restore = 40
        self.center = initiator.center
        
    def execute(self):
        self.center = self.initiator.center
        self.restore_hp()
        self.duration -= 1 #ensure it is never less than 0 by using property
        self.check_blit()
        
    def restore_hp(self):
        col = self.check_collision(self.center,self.targets)
        if col != (-1,-1): self.targets[col[0]].receive_dmg(int(self.restore/v.FPS))

class FireBall(Cast):
    def __init__(self, initiator):
        super(FireBall, self).__init__(initiator, 2*v.FPS)
        self.img_ref = 'fireball'
        self.targets = initiator.enemies
        self.dmg = -40
        self.center = initiator.center
        self.speed = 300
        self.dest = pygame.mouse.get_pos()
        self.attributes = ['flammable']
        self.states['ablaze'] = True
        self.col_ls = [1]
        
    def execute(self):
        self.move_to()
        self.hit()
        self.check_states()
        #self.check_cast_interaction()
        self.duration -= 1 #ensure it is never less than 0 by using property
        self.check_blit()
        
    def check_states(self):
        if not self.states['ablaze']:
            self.duration = 0
            
    def check_cast_interaction(self):
        collisions = pygame.sprite.spritecollide(self,v.current_lvl.casts, False)
        if len(collisions) > 0:
            flammables = [c for c in collisions if 'flammable' in c.attributes and fn.overlap(c.col_ls,self.col_ls)]
            freezables = [c for c in collisions if 'freezable' in c.attributes and fn.overlap(c.col_ls,self.col_ls)]
            fertiles = [c for c in collisions if 'fertile' in c.attributes and fn.overlap(c.col_ls,self.col_ls)]
            conductives = [c for c in collisions if 'conductive' in c.attributes and fn.overlap(c.col_ls,self.col_ls)]
            
            for c in freezables:
                if 'flammable' in self.attributes:
                    if self.states['ablaze']:
                        self.states['ablaze'] = False
                        if c.states['frozen']:
                            c.states['frozen'] = False
                        
            for c in fertiles:
                if 'flammable' in self.attributes:
                    if self.states['ablaze'] and c.states['blooming']:
                        c.states['blooming'] = False
        
    def hit(self):
        col = self.check_collision(self.center,self.targets)
        if col != ([],[]):
            target = [col[0][0],col[1][0]][0]
            target.receive_dmg(int(self.dmg/v.FPS))
            self.duration = v.FPS/58
            
class WaterJet(Cast):
    def __init__(self, initiator):
        super(WaterJet, self).__init__(initiator, 10*v.FPS)
        self.img_ref = 'ice'
        self.targets = initiator.enemies
        self.dmg = -40
        self.center = initiator.center
        self.speed = 150
        self.dest = pygame.mouse.get_pos()
        self.attributes = ['freezable','conductive']
        self.states['frozen'] = True
        self.col_ls = [1]

    def execute(self):
        self.move_to()
        self.hit()
        #self.check_cast_interaction()
        self.check_states()
        self.duration -= 1 #ensure it is never less than 0 by using property
        self.check_blit()
        
    def check_states(self):
        if not self.states['frozen']:
            self.img_ref = 'water'
            self.col_ls = [0]
        if self.states['frozen']:
            self.img_ref = 'ice'
            self.col_ls = [0,1]

                    
    def check_cast_interaction(self):
        collisions = pygame.sprite.spritecollide(self,v.current_lvl.casts, False)
        if len(collisions) > 0:
            flammables = [c for c in collisions if 'flammable' in c.attributes and fn.overlap(c.col_ls,self.col_ls)]
            freezables = [c for c in collisions if 'freezable' in c.attributes and fn.overlap(c.col_ls,self.col_ls)]
            fertiles = [c for c in collisions if 'fertile' in c.attributes and fn.overlap(c.col_ls,self.col_ls)]
            conductives = [c for c in collisions if 'conductive' in c.attributes and fn.overlap(c.col_ls,self.col_ls)]
            
            
            for c in flammables:
                if 'freezable' in self.attributes:
                    if c.states['ablaze']:
                        c.states['ablaze'] = False
                        if self.states['frozen']:
                            self.states['frozen'] = False
            
            for c in freezables:
                if 'freezable' in self.attributes:
                    if self.states['frozen']:
                        if not c.states['frozen']:
                            c.states['frozen'] = True                        
        
    def hit(self):
        col = self.check_collision(self.center,self.targets)
        if col != ([],[]):
            target = [col[0][0],col[1][0]][0]
            target.receive_dmg(int(self.dmg/v.FPS))
            self.duration = v.FPS/58


#class CAC(Cast):
#    def __init__(self, initiator):
#        super(CAC).__init__(initiator, v.FPS/2)
#        self.dps = -50
#        
#    def execute(self):
#        self.deal_dmg()
#        self.duration -= 1 #ensure it is never less than 0 by using property
#        self.check_blit()
#
#    def deal_dmg(self):
#        for t in targets:
#            if t and self collide: t.receive_dmg(int(self.dps/v.FPS))
#
# 