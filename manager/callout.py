# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:03:04 2016

@author: Julien
"""
import variables as v

class Callout():
    @staticmethod
    def listen_and_execute_callouts(group):
         for sprite in group:
             sprite.listen(v.current_lvl.casts,1.1)
         for sprite in group:
             sprite.execute_callouts()
            