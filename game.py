# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:49:27 2016

@author: Julien
"""

import pygame
from pygame.locals import*

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.SRCALPHA, 32)

import random
import sys
import functions as fn
from levels import Level
import variables as v
import characters as ch
import manager.callout as manC 
import data


'''Game Init'''
class Game():
    def __init__(self):
        self.clock = pygame.time.Clock() #set timer which is used to slow game down
        self.screen = screen
        self.levels = [Level(self)]
        v.current_lvl = self.levels[0]
        
        '''clicks'''
        self.pressed_left_clic = False
        self.pressed_right_clic = False
        self.pressed_mid_clic = False

    def run(self):
        while True:
            frame_speed = self.clock.tick(60)
            v.FPS = 1000./frame_speed# self.clock.get_fps()
            self.level_run(v.current_lvl)

    def level_run(self,level):
        self.screen.blit(level.bg,(0,0))

        for event in pygame.event.get(): #setting up quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                print 'has quit'
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    print 'has quit'
                elif event.key == K_t:
                    level.player.cast('t')
                
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 3:
                    self.pressed_right_clic = True
                    level.player.cast('RMB')
                elif event.button == 1:
                    self.pressed_left_clic = True
                    level.player.cast('LMB')
                elif event.button == 2:
                    self.pressed_mid_clic = True
                    level.player.cast('MMB')
                    
            elif event.type == MOUSEBUTTONUP:
                if event.button == 2:
                    self.pressed_mid_clic = False                    
                elif event.button == 3:
                    self.pressed_right_clic = False 
                elif event.button == 1:
                    self.pressed_left_clic = False
                    
#        #next line needs to be after all sprites have been added to the game            
#        self.collisions = pygame.sprite.groupcollide(self.casts,self.casts,False,False, collided = fn.col_lvl_collisions)

        if self.pressed_left_clic: level.player.set_dest()
        if random.randint(0,100) == 0: level.enemy.set_dest((random.randint(250,250),250))
            
        
        manC.Callout.listen_and_execute_callouts(level.casts)
        level.all_sprites.update()

        for s in level.to_blit:
            self.screen.blit(data.images[s.img_ref],s.blit_pos)
            
        
        pygame.display.update()
            
            
Game().run()