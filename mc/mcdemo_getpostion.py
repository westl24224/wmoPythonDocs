#westley Owens
#minecraft position




#load the mincraft modules
from mcpi.minecraft import Minecraft
#create a class called mc
mc = Minecraft.create()
#get the players position
pos = mc.player.getTilePos()
#save that variable in minecraft chat
mc.postToChat(pos)
mc.postToChat("Your X position: " + str(pos.x))
mc.postToChat("Your Y position: " + str(pos.y))
mc.postToChat("Your Z position: " + str(pos.z))