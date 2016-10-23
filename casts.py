# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:49:52 2016

@author: Julien
"""
import pygame
import variables as v
from sprite import MySprite



class Cast(MySprite):
    def __init__(self, initiator,  duration):
        super(Cast, self).__init__()
        self.initiator = initiator
        self.targets = initiator.enemies
        self.duration = duration
        self.attributes = ['flamable','freezable','conductive','fertile']
        self.states = {'ablaze' : False, 
                       'frozen' : False, 
                       'electrified' : False,
                       'blooming': False}

    def execute(self):
        pass
    
    def check_blit(self):
        if self.duration > 0:
            v.current_lvl.to_blit.add(self) 
        else:
            v.current_lvl.to_blit.remove(self)
            
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
class Spell(Cast):
    def __init__(self, initiator):
        super(Spell, self).__init__(initiator, v.FPS/2)
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
