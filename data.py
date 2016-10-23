# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 18:40:57 2016

@author: Julien
"""

import pygame
import random
import functions as fn

colors = [(0,0,0),(255,0,0),(0,255,0),(0,0,255),(50,50,0),(0,50,50),(50,0,50)]
images = {'square': fn.make_surf(50,50,random.choice(colors))}
