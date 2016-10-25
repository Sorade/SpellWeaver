# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:49:27 2016

@author: Julien
"""

import pygame
from pygame.locals import*
import random
import sys
import functions as fn
from levels import Level
import variables as v
import characters as ch

'''Game Init'''
class Game():
    def __init__(self):
        pygame.mixer.init()
        pygame.init()
        self.clock = pygame.time.Clock() #set timer which is used to slow game down
        self.screen = pygame.display.set_mode((800, 600), pygame.SRCALPHA, 32)
        self.levels = [Level(self)]
        v.current_lvl = self.levels[0]

    def run(self):
        while True:
            #v.FPS = self.clock.tick(60)
            frame_speed = self.clock.tick(60)
            v.FPS = 1000./frame_speed# self.clock.get_fps()
            v.current_lvl.run()
            
            
Game().run()