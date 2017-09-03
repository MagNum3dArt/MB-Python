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
subStr = "Move"




def makeUniq(name):
    for take in lSystem.Scene.Takes:
        if take.Name == name:
            name = take.Name + "_1"
            makeUniq(name)
    
    return name


    
    
# app.FileAppend(lFp.FullFilename, True, None)
def merge(lFilePath,subStr):
# Get import file take info
    lOptions = FBFbxOptions( True, lFilePath )
# Tell that by default we won't save anythig except animation. 
    lOptions.SetAll(FBElementAction.kFBElementActionDiscard, True)
# Disable merging of all import file takes
    for lTakeIndex in range( lOptions.GetTakeCount() ):
        if subStr in lOptions.GetTakeName( lTakeIndex):
            lOptions.SetTakeDestinationName( lTakeIndex, makeUniq(lOptions.GetTakeName( lTakeIndex)))
            lOptions.SetTakeSelect( lTakeIndex, True )
        else:
            lOptions.SetTakeSelect( lTakeIndex, False )
# Enable merging of only the first import file take
    #lOptions.SetTakeSelect( 0, True )
# Merge it like it's hot
    lApp.FileMerge( lFilePath , False, lOptions )

def getFile():
    lFp = FBFilePopup()
    lFp.Caption = "Prop Menu Merge: Select a file"
    lFp.Style = FBFilePopupStyle.kFBFilePopupOpen
## options = FBFbxOptions(True)
    lFp.Filter = "*"
    lFp.Path = "D:/_Work/HomeWork/MotionBuilder/ScriptsTesting/MergeTakes"
    lRes = lFp.Execute()
    lFilePath =lFp.FullFilename
    
    return lFilePath
    
def main():
    
    # Select directory you would like to load your FBX files in from 
    # Create the popup and set necessary initial values.
    lFp.Caption = "Source Files: Select the folder containing the files you would like to export"
    
    # Set the default path. Good for a PC only... will have to be different for Mac.
    lFp.Path = r"D:\_Work\HomeWork\MotionBuilder\ScriptsTesting\MergeTakes"
    
    # Get the GUI to show.
    lRes = lFp.Execute()
    
    # If you select a folder, show its name, otherwise indicate that the selection was canceled.
    if not lRes:
        FBMessageBox( "Warning:", "Selection canceled, cannot continue!", "OK" )
    
    else:
        FBMessageBox( "Selected Folder Path:", "Selected folder:\n  Path: '%s'" % lFp.Path, "OK" )
    
 
    
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
        print "fbxList", fbxList
        for fname in fbxList:
            
            print "fileList", fname
    
            lFilePath = lFp.Path + "\\" + fname
            
            merge(lFilePath, subStr)
    
    
if __name__ in ('__name__', '__builtin__'):
    main()
    
    
