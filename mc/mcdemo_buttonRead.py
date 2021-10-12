#Westley Owens
#have it read a button list

#imports Minecraft
from mcpi.minecraft import Minecraft
#create a class called mc
mc = Minecraft.create()
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Set up each pin Number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)



read = ["test"]
while True:   
    if GPIO.input(6) == GPIO.LOW:
        pos = mc.player.getTilePos()
        blockData = mc.getBlock(pos.x, pos.y - 1, pos.z)
        print(blockData)
        print("button 6 was pressed")
        if blockData == 57:
            pos = mc.player.getTilePos()
            mc.player.setPos(pos.x, pos.y + 1000, pos.z)
        
