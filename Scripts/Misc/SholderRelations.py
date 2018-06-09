from pyfbsdk import *


marker = FBModelMarker('m_root')
clavicleXtra = FBFindModelByLabelName('Bip01-L-Clavicle-Xtra')
marker.Visible = True
marker.Show = True


marker.Color = FBColor (1, 1, 0)

marker.Look = FBMarkerLook.kFBMarkerLookHardCross

marker.Translation = FBVector3d(clavicleXtra.Translation)

GV = FBVector3d()
clavicleXtra.GetVector(GV, FBModelTransformationType.kModelTranslation, True)


marker.Translation = GV
print GV
print clavicleXtra.Translation

lMgr = FBConstraintManager()

for i in range (20):
    lCnst = lMgr.TypeCreateConstraint(i)
    
    
lCnst = lMgr.TypeCreateConstraint(7)


