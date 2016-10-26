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
    def __init__(self, img_ref, center, speed, initiator, targets, duration, attributes, col_ls, callouts):
        super(Cast, self).__init__(img_ref, center, speed, callout = callouts)
        self.initiator = initiator
        self.targets = targets
        self.duration = duration
        self.col_ls = col_ls
        self.attributes = attributes#['flammable','freezable','conductive','fertile']
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
                       
    def update(self):
        self.move_to()
        self.hit()
        self.check_states()
        self.duration -= 1 #ensure it is never less than 0 by using property
        self.check_blit()           
                       
                       
    def execute(self):
        pass
    
    
    def check_states(self):
        pass
    
    def hit(self):
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
        super(FireBall, self).__init__('fireball', initiator.center, 300, initiator, initiator.enemies, 10*v.FPS, ['flammable'], [1], ['fire'])
        self.dmg = -40
        self.dest = pygame.mouse.get_pos()
        self.states['ablaze'] = True
        
    def execute_callouts(self): #executes callouts received
        if 'water' in self.received_callouts or 'ice' in self.received_callouts:
            self.states['ablaze'] = False
            self.callouts_save = [ x for x in self.callouts_save if x != 'fire' ]
        
    def check_states(self):
        if not self.states['ablaze']:
            self.duration = 0
            
        
    def hit(self):
        col = self.check_collision(self.center,self.targets)
        if col != ([],[]):
            target = [col[0][0],col[1][0]][0]
            target.receive_dmg(int(self.dmg/v.FPS))
            self.duration = 0#v.FPS/58
            
class WaterJet(Cast):
    def __init__(self, initiator):
        super(WaterJet, self).__init__('ice', initiator.center, 150, initiator, initiator.enemies, 10*v.FPS, ['freezable','conductive'], [1], ['ice'])
        self.dmg = -40
        self.dest = pygame.mouse.get_pos()
        self.states['frozen'] = True

        
    def check_states(self):
        if not self.states['frozen']:
            self.img_ref = 'water'
            self.col_ls = [0]
        if self.states['frozen']:
            self.img_ref = 'ice'
            self.col_ls = [0,1]
            
    def execute_callouts(self): #executes callouts received
        if 'fire' in self.received_callouts:
            self.states['frozen'] = False
            self.add_save_callout('water')
            self.callouts_save = [ x for x in self.callouts_save if x != 'ice' ]
        elif 'ice' in self.received_callouts:
            self.states['frozen'] = True
            self.add_save_callout('ice')
        
    def hit(self):
        col = self.check_collision(self.center,self.targets)
        if col != ([],[]):
            target = [col[0][0],col[1][0]][0]
            target.receive_dmg(int(self.dmg/v.FPS))
            self.duration = 0#v.FPS/58

class MakeTree(Cast):
    def __init__(self, initiator):
        super(MakeTree, self).__init__('tree', initiator.center, 150, initiator, initiator.enemies, 10*v.FPS, ['fertile','flammable'], [0,1], [])
        self.dmg = -40
        self.dest = pygame.mouse.get_pos()
        self.states['blooming'] = True

    def check_states(self):
        if not self.states['blooming']:
            self.img_ref = 'dead_tree'
        if self.states['blooming']:
            self.img_ref = 'tree'
            
    def execute_callouts(self): #executes callouts received
        '''make a received_callouts attributes and set() them, then, filter them in order:
        fire, water, fertile, elec'''
        if 'water' in self.received_callouts:
            self.states['blooming'] = True
            self.callouts_save = [ x for x in self.callouts_save if x != 'fire' ]
        elif 'fire' in self.received_callouts:
            self.states['blooming'] = False
            self.add_save_callout('fire')
            self.callouts_save = [ x for x in self.callouts_save if x != 'water' or x!= 'ice' ]
                
        
    def hit(self):
        col = self.check_collision(self.center,self.targets)
        if col != ([],[]):
            target = [col[0][0],col[1][0]][0]
            target.receive_dmg(int(self.dmg/v.FPS))
            self.duration = 0#v.FPS/58
