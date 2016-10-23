# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:43:04 2016

@author: s0939551
"""
'''import built in modules'''
import pygame
from pygame.locals import*
import random
import sys
import functions as fn

'''Game Init'''
pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock() #set timer which is used to slow game down


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        self.hp = 500
        self.img_ref = 'square'
        self.center = (100,100)
        self.speed = 25 #px/s
        self.type = 'human'
        self.dest = (0,0)
        self.obstacles = []
        self.enemies = []
        self.allies = []
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
            
#    def check_collision(self,new_pos):
#        for o in self.obstacles:
#            if rect.o collides with Rect(new_pos is the center):
#                return True
#        return False
        
    def move_to(self):
        mvt_ratio = (self.speed/FPS)/fn.dist(self.center,self.dest)
        dx,dy = self.dest[0] - self.center[0] ,self.dest[1] - self.center[1]
        new_pos = fn.sum_tulp(self.center,(int(dx + dx * mvt_ratio),int(dy + dy * mvt_ratio)))
#        if not self.check_collision(new_pos): self.center = new_pos
        self.center = new_pos
    
    '''Combat Logic'''

    def cast(self,current_clicked, pos):
        self.casts[current_clicked](self, pos)
        
    def receive_dmg(self,dmg):
        self.hp += dmg
        if self.hp <= 0:
            self.dead = True
        else:
            self.dead = False
        
#class Cast(MySprite):
#    def __init__(self, initiator,  pos, duration):
#        super
#        self.initiator = initiator
#        self.targets = initiator.enemies
#        self.pos = pos
#        self.duration = duration
#        self.creation_time = current_time
#
#    def execute(self):
#        pass
#    
#    def check_blit(self):
#        if self.duration > 0:
#            add_to_blit_group #a variable
#        else:
#            remove
#            
#class CAC(Cast):
#    def __init__(self, initiator, pos):
#        super(CAC).__init__(initiator, pos, FPS/2)
#        self.dps = -50
#        
#    def execute(self):
#        self.deal_dmg()
#        self.duration -= 1 #ensure it is never less than 0 by using property
#        self.check_blit()
#
#    def deal_dmg(self):
#        for t in targets:
#            if t and self collide: t.receive_dmg(int(self.dps/FPS))
#
#    
#class Spell(Cast):
#    def __init__(self, initiator, pos):
#        super(CAC).__init__(initiator, pos, FPS/2)
#        self.targets = initiator.allies
#        self.restore = 40
#        
#    def execute(self):
#        self.restore_hp()
#        self.duration -= 1 #ensure it is never less than 0 by using property
#        self.check_blit()
#        
#    def restore_hp(self):
#        for t in targets:
#            if t and self collide: t.receive_dmg(int(self.restore/FPS)):
                
ms = MySprite()
screen = pygame.display.set_mode((800, 600), pygame.SRCALPHA, 32)
black_bg = pygame.Surface((800,600))
black_bg.fill((200,200,200))
black_bg.set_alpha(100)
FPS = 60

class Level():

    
    def run(self):
        screen.blit(black_bg,(0,0))
        for event in pygame.event.get(): #setting up quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                print 'has quit'
            elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                print 'has quit'
                
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 3:
                    self.pressed_right_clic = True
                elif event.button == 1:
                    self.pressed_left_clic = True
                    ms.set_dest()
                    ms.move_to()
                elif event.button == 2:
                    self.pressed_mid_clic = True
                elif event.button == 4:
                    self.interface.delta += 1
                elif event.button == 5:
                    self.interface.delta -= 1
                    
            elif event.type == MOUSEBUTTONUP:
                if event.button == 2:
                    self.pressed_mid_clic = True                    
                elif event.button == 3:
                    self.pressed_right_clic = True 
                elif event.button == 1:
                    self.pressed_left_clic = True

        screen.blit(pygame.Surface((50,50)),ms.center)
        pygame.display.update()
#            when LMB:
#                player.cast(LMB, mouse.pos)
        
#        for s in non_players:
#            s.act()
#            
#        for c in casts:
#            c.deal_dmg()
            
#        for s in sprites_to_blit:
#            blit s

class A():
    def __init__(self):
        self.val = [1,2,3]
        
    def edit(self):
        self.val += [4]
        
class B():
    def __init__(self, x):
        self.x = x
while True:
    Level().run()