import os
import re
from pyfbsdk import *
from pyfbsdk_additions import *

# Creating all the Constructors
lFp = FBFolderPopup()
lDFp = FBFolderPopup()
lSystem = FBSystem()
lApp = FBApplication ()
lScene = lSystem.Scene


fbxList = []
subStr = "Move"
edits = {}

def getUniqNumber():
    lTime = FBSystem().SystemTime
    uniq_number = str(lTime.GetSecondDouble()).split(".")
    uniq_number = uniq_number[1]
    return uniq_number
    

def makeUniq(name):
    for take in lSystem.Scene.Takes:
        if take.Name == name:
            name = take.Name + "_copy_" + getUniqNumber() + getUniqNumber()
            makeUniq(name)
    
    return name


def BtnFileCallback(control,event):
    lFp = FBFilePopup()
    lFp.Caption = "Prop Menu Merge: Select a file"
    lFp.Style = FBFilePopupStyle.kFBFilePopupOpen
    lFp.Filter = "*"
    lFp.Path = "D:/_Work/HomeWork/MotionBuilder/ScriptsTesting/MergeTakes"
    lRes = lFp.Execute()
    if not lRes:
        FBMessageBox( "Warning:", "Selection canceled, cannot continue!", "OK" )
    
    else:
        lFilePath =lFp.FullFilename
        edits['File'].Text = lFilePath
    



def BtnImportCallback(control,event):
    lFilePath = edits['File'].Text
    subStr = edits['Find'].Text
    merge(lFilePath, subStr)
    
# app.FileAppend(lFp.FullFilename, True, None)
def merge(lFilePath,subStr):
# Get import file take info
    lOptions = FBFbxOptions( True, lFilePath )
# Tell that by default we won't save anythig except animation. 
    lOptions.SetAll(FBElementAction.kFBElementActionDiscard, True)
# Disable merging of all import file takes
    for lTakeIndex in range( lOptions.GetTakeCount() ):
        if subStr in lOptions.GetTakeName( lTakeIndex):
            if edits["Overwrite"].State==False:
                lOptions.SetTakeDestinationName( lTakeIndex, makeUniq(lOptions.GetTakeName( lTakeIndex)))
            lOptions.SetTakeSelect( lTakeIndex, True )
        else:
            lOptions.SetTakeSelect( lTakeIndex, False )
# Enable merging of only the first import file take
    #lOptions.SetTakeSelect( 0, True )
# Merge it like it's hot
    lApp.FileImport( lFilePath , True, False)

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
    l.Caption = "Find takes with: "
    x = FBAddRegionParam(10,FBAttachType.kFBAttachLeft,"")
    y = FBAddRegionParam(10,attachType,anchor)
    w = FBAddRegionParam(75,FBAttachType.kFBAttachNone,"")
    h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
    
    mainLyt.AddRegion(labId,labId, x, y, w, h)
    mainLyt.SetControl(labId,l)


        
    # Create edit
    editId = "EditFind"
    e = FBEdit()
    edits['Find'] = e
    
    x = FBAddRegionParam(10,FBAttachType.kFBAttachRight,labId)
    y = FBAddRegionParam(10,attachType,anchor)
    w = FBAddRegionParam(190,FBAttachType.kFBAttachNone,"")
    h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")

    mainLyt.AddRegion(editId,editId, x, y, w, h)

    mainLyt.SetControl(editId,e)
  
    attachType = FBAttachType.kFBAttachBottom
    anchor = labId

    # Create edit
    editId = "EditFile"
    e = FBEdit()
    edits['File'] = e
    
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
    mainLyt.AddRegion("File","File", x, y, w, h)
    lyt = FBHBoxLayout()
    mainLyt.SetControl("File",lyt)

    b = FBButton()
    b.Caption = "File"
    b.Justify = FBTextJustify.kFBTextJustifyCenter
    lyt.Add(b,60)
    b.OnClick.Add(BtnFileCallback)


    
    # Do specific edit initialization according to its type
    
    # Find 
    e = edits['Find']
    e.Text = ""
    #e.PasswordMode = True
    #e.OnChange.Add(SetFind)
    
    e = edits['File']
    e.Text = "D:\_Work\HomeWork\MotionBuilder\ScriptsTesting\MergeTakes"
    #e.PasswordMode = True
    #e.OnChange.Add(SetReplace)
    
    x = FBAddRegionParam(0,FBAttachType.kFBAttachLeft,"")
    y = FBAddRegionParam(80,FBAttachType.kFBAttachTop,"")
    w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
    h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
    mainLyt.AddRegion("Checkbox","Checkbox", x, y, w, h)
    lyt = FBHBoxLayout()
    mainLyt.SetControl("Checkbox",lyt)
    
    b = FBButton()
    b.Caption = "Overwrite existed takes"
    b.Style = FBButtonStyle.kFBCheckbox 
    b.Justify = FBTextJustify.kFBTextJustifyLeft
    lyt.Add(b,200)
    edits['Overwrite'] = b
    
    x = FBAddRegionParam(220,FBAttachType.kFBAttachLeft,"")
    y = FBAddRegionParam(110,FBAttachType.kFBAttachTop,"")
    w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
    h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
    mainLyt.AddRegion("Import","Import", x, y, w, h)
    lyt = FBHBoxLayout()
    mainLyt.SetControl("Import",lyt)
    
    b = FBButton()
    b.Caption = "Import"
    b.Justify = FBTextJustify.kFBTextJustifyCenter
    lyt.Add(b,60)
    b.OnClick.Add(BtnImportCallback)
    
##    b = FBButton()
##    b.Caption = "Rename"
##    b.Justify = FBTextJustify.kFBTextJustifyCenter
##    lyt.Add(b,60)
##    b.OnClick.Add(BtnRenameCallback)

def CreateTool():
    # Tool creation will serve as the hub for all other controls
    t = FBCreateUniqueTool("Import Takes")
    t.StartSizeX = 300
    t.StartSizeY = 200

    PopulateLayout(t)
    ShowTool(t)
    


if __name__ in ('__name__', '__builtin__'):
##    main()
    CreateTool()
    
    
