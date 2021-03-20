# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:16:33 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()
mc.postToChat("i'm watching you")

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("you are located on X:"+str(x)+",Y:"+str(y)+",Z:"+str(z))