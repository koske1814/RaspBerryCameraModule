#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys
import sg90

s = sg90.sg90(12,0)

def photoView():
    s.setdirection(45,10)    
    time.sleep(0.5)
    s.setdirection(0,10)
    time.sleep(0.5)
    s.setdirection(-45,-10)
    time.sleep(0.5)
    s.setdirection(0,10)
    time.sleep(0.5)
   
