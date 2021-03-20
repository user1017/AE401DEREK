# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:10:01 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()
import time
time.sleep(5)
x,y,z=mc.player.getTilePos()


mc.player.setTilePos(x,y,z)
time.sleep(0.5)
x=x+100
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y-100
mc.player.setTilePos(x,y,z)