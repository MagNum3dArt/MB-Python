from pyfbsdk import *
from pyfbsdk_additions import *

import random

def CreateCube(xPos,yPos,scaleFactor):
    name = "тестовый кубик _%d_%d" % (xPos,yPos)
    cube = FBModelCube(name)
    cube.Show = True
    
    cube.Translation = FBVector3d(xPos,yPos,0)
    cube.Scaling = FBVector3d(scaleFactor,scaleFactor,scaleFactor)
    
    return cube


def main():
    GAB_INTERVAL = 50
    for xPos in range(-500,500,GAB_INTERVAL):
        for yPos in range(0,1000,GAB_INTERVAL):
            CreateCube(xPos,yPos,(random.random()*5.0 +5.0))
            
            
if __name__ in ('__name__', '__builtin__'):
    main()
    