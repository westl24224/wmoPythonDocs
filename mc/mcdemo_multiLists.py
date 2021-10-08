#westley Owens
#create a multi dimnesional list
from mcpi.minecraft import Minecraft
#create a class called mc
mc = Minecraft.create()

#make a line of wool color
woolLine = [13, 12, 8, 7, 1]
#thi sis will print a gird of wool block    
woolGrid = [[5, 5, 5, 13, 13, 13, 5, 5, 0-,]
            ]
pos = mc.player.getTilePos()
#this loop will place a line of wool
'''
for i, wool in  enumerate (woolLine):
    print(str(i) + " is the color " + str(wool))
    mc.setBlock(pos.x + i, pos.y, pos.z, 35, wool)
'''


for i, row in enumerate (woolGrid):
    print(row)
    for j, col in enumerate(row):
        print(col)
        mc.setBlock(pos.x + j, pos.y + i, pos.z, 35, col)
        