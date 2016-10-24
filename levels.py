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
        self.player = ch.Human((100,100),'human')
        self.enemy = ch.Orc((250,250))
        black_bg = pygame.Surface((800,600))
        black_bg.fill((200,200,200))
        black_bg.set_alpha(100)
        self.bg = black_bg
        
        self.all_sprites = pygame.sprite.Group(self.player,self.enemy)
        self.all_characters = pygame.sprite.Group(self.player,self.enemy)

        self.assign_obstacles()
        self.assign_enemies()
        
        self.casts = pygame.sprite.Group()
        self.to_blit = pygame.sprite.Group(self.player,self.enemy)
        
        '''clicks'''
        self.pressed_left_clic = False
        self.pressed_right_clic = False
        self.pressed_mid_clic = False
        
    def assign_obstacles(self):
        for s in self.all_sprites:
            [s.obstacles.add(ss) for ss in self.all_sprites if ss != s]
            
    def assign_enemies(self):
        for s in self.all_characters:
            [s.enemies.add(ss) for ss in self.all_characters if ss.cat in s.enemy_cats]
        
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
                    self.player.cast('RMB',1)
                elif event.button == 1:
                    self.pressed_left_clic = True
                    self.player.cast('LMB',1)
                elif event.button == 2:
                    self.pressed_mid_clic = True
                    self.player.cast('MMB',1)
                    
            elif event.type == MOUSEBUTTONUP:
                if event.button == 2:
                    self.pressed_mid_clic = False                    
                elif event.button == 3:
                    self.pressed_right_clic = False 
                elif event.button == 1:
                    self.pressed_left_clic = False

        if self.pressed_left_clic: self.player.set_dest()
        if random.randint(0,100) == 0: self.enemy.set_dest((random.randint(50,450),250))
        for s in self.all_sprites:
            s.move_to()
        
        #self.update_states()
        for c in self.casts:
            c.execute()
        for c in self.casts:
            c.callouts = list(c.callouts_save)

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

    def update_states(self):
    
        '''make cast attribute lists'''
        flammables = []
        freezables = []
        fertiles =[]
        conductives = []
        for c in self.casts:
            if 'flammable' in c.attributes: flammables.append(c)
            if 'freezable' in c.attributes: freezables.append(c)
            if 'fetile' in c.attributes: fertiles.append(c)
            if 'conductive' in c.attributes: conductives.append(c)
    
        '''resolve cast states'''
        '''for flammables'''
    
        for f in flammables:
            for c in flammables:
                if c.rect.colliderect(f.rect) and fn.overlap(c.col_ls,f.col_ls):
                    if c is not f and f.states['ablaze']:
                        c.states['ablaze'] = True
    
            for c in freezables:
                if c.rect.colliderect(f.rect) and fn.overlap(c.col_ls,f.col_ls):
                    if f.states['ablaze']:
                        if c.states['frozen']:
                            c.states['frozen'] = False
                        f.states['ablaze'] = False
    
            for c in fertiles:
                if c.rect.colliderect(f.rect) and fn.overlap(c.col_ls,f.col_ls):
                    if f.states['ablaze'] and c.states['fertile']:
                        c.states['fertile'] = False
    
        '''for freezables'''
    
        for w in freezables:
            for c in freezables:
                if c.rect.colliderect(w.rect) and fn.overlap(c.col_ls,w.col_ls):
                    if c is not w and w.states['frozen']:
                        c.states['frozen'] = True
    
            for c in fertiles:
                if c.rect.colliderect(w.rect) and fn.overlap(c.col_ls,w.col_ls):
                    if w.states['frozen']:
                        c.states['blooming'] =  False
                    elif not w.states['frozen']:
                        c.states['blooming'] = True
    
            for c in conductives:
                if c.rect.colliderect(w.rect) and fn.overlap(c.col_ls,w.col_ls):
                    if not w.states['frozen'] and c.states['electrified']:
                        w.states['electrified'] = True
                    elif w.states['frozen']:
                        w.states['electrified'] = False
    
        '''for fertiles'''
    
        for f in fertiles:
            for c in fertiles:
                if f is not c and fn.overlap(c.col_ls,f.col_ls) and  c.rect.colliderect(f.rect) :
                    if f.states['blooming']:
                        c.states['blooming'] =  True
    
            for c in conductives:
                if  c.rect.colliderect(f.rect)  and fn.overlap(c.col_ls,f.col_ls):
                    if f.states['blooming'] and c.states['electrified']:
                        f.states['blooming'] = False
    
        '''for conductives'''
    
        for e in conductives:
            for c in conductives:
                if fn.overlap(c.col_ls,e.col_ls) and  c.rect.colliderect(e.rect) :
                    if e is not c and e.states['electrified']:
                        c.states['electrified'] =  True