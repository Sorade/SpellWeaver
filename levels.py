# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:51:15 2016

@author: Julien
"""

import pygame
from pygame.locals import*
import random
import sys
import functions as fn
import variables as v
import characters as ch
import data


class Level():
    def __init__(self,game):
        self.game = game
        self.player = ch.Character((100,100),'human')
        self.enemy = ch.Character((250,250))
        black_bg = pygame.Surface((800,600))
        black_bg.fill((200,200,200))
        black_bg.set_alpha(100)
        self.bg = black_bg
        self.all_sprites = pygame.sprite.Group(self.player,self.enemy)
        self.assign_obstacles()
        self.casts = pygame.sprite.Group()
        self.to_blit = pygame.sprite.Group(self.player,self.enemy)
        
        '''clicks'''
        self.pressed_left_clic = False
        self.pressed_right_clic = False
        self.pressed_mid_clic = False
        
    def assign_obstacles(self):
        for s in self.all_sprites:
            s.obstacles = s.obstacles + [ss for ss in self.all_sprites if ss != s]
        
    def run(self):
        self.game.screen.blit(self.bg,(0,0))
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
                elif event.button == 2:
                    self.pressed_mid_clic = True
                elif event.button == 4:
                    self.interface.delta += 1
                elif event.button == 5:
                    self.interface.delta -= 1
                    
            elif event.type == MOUSEBUTTONUP:
                if event.button == 2:
                    self.pressed_mid_clic = False                    
                elif event.button == 3:
                    self.pressed_right_clic = False 
                elif event.button == 1:
                    self.pressed_left_clic = False

        if self.pressed_left_clic: self.player.set_dest()
        if self.pressed_right_clic: self.player.cast(1,1)
        if random.randint(0,100) == 0: self.enemy.set_dest((random.randint(50,450),250))
        for s in self.all_sprites:
            s.move_to()
            
        for c in self.casts:
            c.execute()

        for s in self.to_blit:
            self.game.screen.blit(data.images[s.img_ref],s.blit_pos)
        
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
