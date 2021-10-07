#Westkey Owens
#Places randomly places colored wools
from mcpi.minecraft import Minecraft
#create a class called mc
mc = Minecraft.create()
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Set up each pin Number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#set up program from MC and two buttons'
#create a counter variable that starts at zero
#create a list of block data of the color of wool
#Define a function called place next
#    it take one argument named dirrection
#    it changes the counter by adding the direction to the argument
#    place a wool block of that color from the the list where the index matched the counter
#in a forevere loop
#    if the first button was pressed, placeNext(+1)
#    if the second button was pressed, placeNext(-1)

counter = 0
woolColor = [0, 1, 2] 


def placeNext(direction):
    global counter
    counter += direction
    if counter > 2:
        counter = 0
    if counter < 0:
        counter = 0
    mc.setBlock(11, 5, 14, 35,woolColor[counter])
while True:
    if GPIO.input(6) == GPIO.LOW:
        placeNext(1)
    if GPIO.input(13) == GPIO.LOW:
        placeNext(-1)




placeNext()