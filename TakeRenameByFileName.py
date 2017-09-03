import os
import re
from pyfbsdk import *

# Creating all the Constructors
lFp = FBFolderPopup()
lDFp = FBFolderPopup()
##lMgr = FBFbxManager()
lSystem = FBSystem()
lApp = FBApplication ()
lScene = lSystem.Scene
fbxList = []

# Select directory you would like to load your FBX files in from 
# Create the popup and set necessary initial values.
lFp.Caption = "Source Files: Select the folder containing the files you would like to export"

# Set the default path. Good for a PC only... will have to be different for Mac.
lFp.Path = r"d:\Work\Projects\VR\Characters\Girl\V1\Production\scenes\Hit_Reaction"

# Get the GUI to show.
lRes = lFp.Execute()

# If you select a folder, show its name, otherwise indicate that the selection was canceled.
if not lRes:
    FBMessageBox( "Warning:", "Selection canceled, cannot continue!", "OK" )

else:
    FBMessageBox( "Selected Folder Path:", "Selected folder:\n  Path: '%s'" % lFp.Path, "OK" )
    
    lDFp.Caption = "Destanation Folder: Select the folder for export"
    
    # Set the default path. Good for a PC only... will have to be different for Mac.
    lDFp.Path = lFp.Path
    
    # Get the GUI to show.
    lDRes = lDFp.Execute()

    # If you select a folder, show its name, otherwise indicate that the selection was canceled.
    if not lDRes:
        FBMessageBox( "Warning:", "Selection canceled, cannot continue!", "OK" )
    
    else:
        FBMessageBox( "Selected Folder Path:", "Selected folder:\n  Path: '%s'" % lDFp.Path, "OK" )




    
        # Getting the names of the files in your previously selected folder
        # Using os to get the file names from the specified folder (above) and storing names of files in a list
        fileList = os.listdir(lFp.Path)
        print "fileList", fileList
        # Setting the regular expression to only look for .fbx extenstion
        fbxRE = re.compile('^\w+.fbx$', re.I)
    
        # Removing any files that do not have an .fbx extenstion
        for fname in fileList:
            mo = fbxRE.search(fname)
            if mo:
                fbxList.append(fname)
        # Exporting items in the file one at a time
        for fname in fbxList:
            
    ##        print "fileList", fname
    
            # Opening the file in MotionBuilder, this replaces the current scene
            lApp.FileOpen(lFp.Path + "\\" + fname)
    
            # Saves out the character and rig animation
            # if there are multiple characters per file you will need to change to accommodate.
            # SaveCharacterRigAndAnimation (str pFileName, FBCharacter pCharacter, bool pSaveCharacter, bool pSaveRig, bool pSaveExtensions)
    
            shortName = fname.split(".")
            shortName = shortName[0]
            newTake = FBSystem().Scene.Takes[0]
            
            newTake.Name = shortName
            lApp.FileSave(lDFp.Path + "\\" + fname)
            #lMgr.SaveCharacterRigAndAnimation(lFp.Path + "\\Animation_" + fname, lScene.Characters[0], False, True, False)
    
            # Closing the current file, not really necessarily needed sine the FBApplication::FileOpne replaces the current scene
            lApp.FileNew()

##app23 = FbxManager()

##longname = app.FBXFileName
##data = longname.split("\\")
##shortName = data[len(data)-1]
##shortName = shortName.split(".")
##shortName = shortName[0]
##print shortName
##newTake = FBSystem().Scene.Takes[0]
##for myTake in FBSystem().Scene.Takes:
##        print myTake.Name
##        
##newTake = FBSystem().Scene.Takes[0]
##newTake.Name = shortName
##print newTake.Name
##app.FileSave("\\export_" + shortName+".fbx")

#Cleanup
del(lFp, lDFp, FBFolderPopup, lSystem, FBSystem, lRes, lApp, FBApplication, lScene, fbxList, re, os, FBMessageBox)

