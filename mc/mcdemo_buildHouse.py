#Westley Owens
#Build a house in minecraft eith buttton


#imports Minecraft
from mcpi.minecraft import Minecraft
#create a class called mc
mc = Minecraft.create()
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Set up each pin Number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#this defines a house
def house():
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x + 1, pos.y, pos.z + 1, pos.x + 6, pos.y + 5, pos.z + 6, 5)
    mc.setBlocks(pos.x + 2, pos.y + 1, pos.z + 2, pos.x + 5, pos.y + 4, pos.z + 5, 0)
    mc.setBlocks(pos.x + 3, pos.y + 1, pos.z + 1, pos.x + 3, pos.y + 2, pos.z + 1, 64)
    mc
    
while True:
    #check the first button
    if GPIO.input(6) == GPIO.LOW:
        print("button 6 was pressed")
        house()