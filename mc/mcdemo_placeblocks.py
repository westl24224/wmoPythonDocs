#mcdemo place.py
#Get the tile position and save it to a variable
#use the current function to place a block under current position
#(under the y -1 )

#load the mincraft modules
from mcpi.minecraft import Minecraft
#create a class called mc
mc = Minecraft.create()
#get the players position
while True:
    pos = mc.player.getTilePos()
    #save that variable in minecraft chat
    mc.postToChat(pos)
    mc.postToChat("Your X position: " + str(pos.x))
    mc.postToChat("Your Y position: " + str(pos.y))
    mc.postToChat("Your Z position: " + str(pos.z))
    mc.setBlock(pos, 1)
    mc.postToChat("set block to stone")