# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 18:40:57 2016

@author: Julien
"""

import pygame
import random
import functions as fn

def img_import(str,dim = None):
    img = pygame.image.load('data\\{}'.format(str)).convert_alpha()
    if dim is not None:
        img = pygame.transform.smoothscale(img,dim)
    return img

colors = [(0,0,0),(255,0,0),(0,255,0),(0,0,255),(50,50,0),(0,50,50),(50,0,50)]
images = {'orc': fn.make_surf(25,50,(0,200,0)), 
          'human' : img_import('sprites\\characters\\human.png'),
          'fireball': fn.make_surf(25,25,(255,10,10)), 
          'water': fn.make_surf(50,50,(0,0,200)), 
          'ice': fn.make_surf(25,50,(0,0,255)), 
          'tree': fn.make_surf(50,75,(0,200,0)),
          'dead_tree': fn.make_surf(50,75,(255,200,0))}
