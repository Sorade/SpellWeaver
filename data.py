# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 18:40:57 2016

@author: Julien
"""

import pygame
import random
import functions as fn

colors = [(0,0,0),(255,0,0),(0,255,0),(0,0,255),(50,50,0),(0,50,50),(50,0,50)]
images = {'orc': fn.make_surf(25,50,(0,200,0)), 
          'human' : fn.make_surf(25,50,(100,75,75)),
          'fireball': fn.make_surf(25,25,(255,10,10)), 
          'water': fn.make_surf(50,50,(0,0,200)), 
          'ice': fn.make_surf(25,50,(0,0,255))}
