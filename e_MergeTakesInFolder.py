import os
import re
from pyfbsdk import *
from pyfbsdk_additions import *

# Creating all the Constructors
lFp = FBFolderPopup()
lDFp = FBFolderPopup()
##lMgr = FBFbxManager()
lSystem = FBSystem()
lApp = FBApplication ()
lScene = lSystem.Scene

fbxList = []
subStr = "Move"
editStyles = ["Find","Replace"]
edits = {}


def makeUniq(name):
    for take in lSystem.Scene.Takes:
        if take.Name == name:
            name = take.Name + "_1"
            makeUniq(name)
    
    return name


def BtnFolderCallback(control,event):
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
        edits['Folder'].Text = lFp.Path
##        FBMessageBox( "Selected Folder Path:", "Selected folder:\n  Path: '%s'" % lFp.Path, "OK" )



def BtnMergeCallback(control,event):
    return
    
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
    
    
def PopulateLayout(mainLyt):
    anchor = ""
    attachType = FBAttachType.kFBAttachTop

    # Generically create different types of edit
    
    # Create label
    labId = "LabelFind"
    l = FBLabel()
    l.Caption = "Find:"
    x = FBAddRegionParam(10,FBAttachType.kFBAttachLeft,"")
    y = FBAddRegionParam(10,attachType,anchor)
    w = FBAddRegionParam(50,FBAttachType.kFBAttachNone,"")
    h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
    
    mainLyt.AddRegion(labId,labId, x, y, w, h)
    mainLyt.SetControl(labId,l)


        
    # Create edit
    editId = "EditFind"
    e = FBEdit()
    edits['Find'] = e
    
    x = FBAddRegionParam(10,FBAttachType.kFBAttachRight,labId)
    y = FBAddRegionParam(10,attachType,anchor)
    w = FBAddRegionParam(200,FBAttachType.kFBAttachNone,"")
    h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")

    mainLyt.AddRegion(editId,editId, x, y, w, h)

    mainLyt.SetControl(editId,e)
  
    attachType = FBAttachType.kFBAttachBottom
    anchor = labId

    # Create edit
    editId = "EditFolder"
    e = FBEdit()
    edits['Folder'] = e
    
    x = FBAddRegionParam(10,FBAttachType.kFBAttachLeft,"")
    y = FBAddRegionParam(10,attachType,anchor)
    w = FBAddRegionParam(200,FBAttachType.kFBAttachNone,"")
    h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")

    mainLyt.AddRegion(editId,editId, x, y, w, h)

    mainLyt.SetControl(editId,e)
  
##    attachType = FBAttachType.kFBAttachBottom
##    anchor = labId


    x = FBAddRegionParam(10,FBAttachType.kFBAttachRight,editId)
    y = FBAddRegionParam(10,attachType,anchor)
    w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
    h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
    mainLyt.AddRegion("main1","main1", x, y, w, h)
    lyt = FBHBoxLayout()
    mainLyt.SetControl("main1",lyt)

    b = FBButton()
    b.Caption = "Folder"
    b.Justify = FBTextJustify.kFBTextJustifyCenter
    lyt.Add(b,60)
    b.OnClick.Add(BtnFolderCallback)


    
    # Do specific edit initialization according to its type
    
    # Find 
    e = edits['Find']
##    e.Text = "Find sub string"
    #e.PasswordMode = True
    #e.OnChange.Add(SetFind)
    
##    e = edits['Replace']
##    e.Text = "Replace with sub string"
    #e.PasswordMode = True
    #e.OnChange.Add(SetReplace)
    
    x = FBAddRegionParam(100,FBAttachType.kFBAttachLeft,"")
    y = FBAddRegionParam(100,FBAttachType.kFBAttachTop,"")
    w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
    h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
    mainLyt.AddRegion("main","main", x, y, w, h)
    lyt = FBHBoxLayout()
    mainLyt.SetControl("main",lyt)
    
    b = FBButton()
    b.Caption = "Merge"
    b.Justify = FBTextJustify.kFBTextJustifyCenter
    lyt.Add(b,60)
    b.OnClick.Add(BtnMergeCallback)
    
##    b = FBButton()
##    b.Caption = "Rename"
##    b.Justify = FBTextJustify.kFBTextJustifyCenter
##    lyt.Add(b,60)
##    b.OnClick.Add(BtnRenameCallback)

def CreateTool():
    # Tool creation will serve as the hub for all other controls
    t = FBCreateUniqueTool("Find and Replace Take Names")
    t.StartSizeX = 300
    t.StartSizeY = 200

    PopulateLayout(t)
    ShowTool(t)
    


if __name__ in ('__name__', '__builtin__'):
##    main()
    CreateTool()
    
    