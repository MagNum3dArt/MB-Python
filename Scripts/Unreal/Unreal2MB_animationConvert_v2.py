from pyfbsdk import *
from pyfbsdk_additions import *

root = FBFindModelByLabelName('root')

# Get the prerotation handle
lProp = root.PropertyList.Find( 'PreRotation' )

# Make a new vector
lV3d = FBVector3d(-190,0,0)


root.Selected = True