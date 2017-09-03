from pyfbsdk import *
from pyfbsdk_additions import *

# Creating all the Constructors
lSys = FBSystem()


editStyles = ["Find","Replace"]

edits = {}

# Normal Edit

def findWarning():
    Selected = 0
    Changed = 0 
    e = edits['Find']
    nameOld = e.Text
    e = edits['Replace']
    nameNew = e.Text
    
    for take in lSys.Scene.Takes:
        if take.Selected:
            Selected = Selected +1
            oldName = take.Name
            newName = oldName.replace(nameOld, nameNew)
            if oldName != newName:
                Changed = Changed + 1

    if Selected == 0:
        FBMessageBox( "Warning:", "There is no selected Takes!", "OK" )
        return True
    if nameOld == '':
        FBMessageBox( "Warning:", "There is nothing to Find!", "OK" )
        return True
    if nameNew == nameOld:
        FBMessageBox( "Warning:", "Replace is the same as Find!", "OK" )
        return True
    if Changed == 0:
        FBMessageBox( "Warning:", "There is no '%s' in selected takes" %edits['Find'].Text, "OK" )
        return True
        
    return False
     


def BtnDelCallback(control,event):
    e = edits['Find']
    nameOld = e.Text
    nameNew = ''

    if findWarning():
        return
    for take in lSys.Scene.Takes:
        if take.Selected:
            take.Name = take.Name.replace(nameOld, nameNew)
    
    FBMessageBox( "Changes:",  "'%s' is deleted in selected Takes" %edits['Find'].Text, "OK" )

def BtnRenameCallback(control,event):
    e = edits['Find']
    nameOld = e.Text
    e = edits['Replace']
    nameNew = e.Text

    if findWarning():
        return
        
##    if  nameNew =='':
##        FBMessageBox( "Warning:", "There is nothing to Replace! To delete substring press 'Del' button.", "OK" )
##        return
        
           
    for take in lSys.Scene.Takes:
        if take.Selected:
            take.Name = take.Name.replace(nameOld, nameNew)

    FBMessageBox( "Changes:",  "'%s' is replaced with '%s' in selected Takes" %(edits['Find'].Text, edits['Replace'].Text), "OK" )
        
##            print take.Name
    
def PopulateLayout(mainLyt):
    anchor = ""
    attachType = FBAttachType.kFBAttachTop

    # Generically create different types of edit
    for style in editStyles:
        # Create label
        labId = "Label" + style
        l = FBLabel()
        l.Caption = style
        x = FBAddRegionParam(10,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(10,attachType,anchor)
        w = FBAddRegionParam(50,FBAttachType.kFBAttachNone,"")
        h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
        
        mainLyt.AddRegion(labId,labId, x, y, w, h)
        mainLyt.SetControl(labId,l)
            
        # Create edit
        editId = "Edit" + style
        initCall = "%s()" % ("FBEdit")
        e = eval( initCall )
        edits[style] = e
        
        x = FBAddRegionParam(10,FBAttachType.kFBAttachRight,labId)
        y = FBAddRegionParam(10,attachType,anchor)
        w = FBAddRegionParam(200,FBAttachType.kFBAttachNone,"")
        h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
    
        mainLyt.AddRegion(editId,editId, x, y, w, h)
    
        mainLyt.SetControl(editId,e)
      
        attachType = FBAttachType.kFBAttachBottom
        anchor = labId
        
    # Do specific edit initialization according to its type
    
    # Find 
    e = edits['Find']
##    e.Text = "Find sub string"
    #e.PasswordMode = True
    #e.OnChange.Add(SetFind)
    
    e = edits['Replace']
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
    
##    b = FBButton()
##    b.Caption = "Del"
##    b.Justify = FBTextJustify.kFBTextJustifyCenter
##    lyt.Add(b,60)
##    b.OnClick.Add(BtnDelCallback)
    
    b = FBButton()
    b.Caption = "Rename"
    b.Justify = FBTextJustify.kFBTextJustifyCenter
    lyt.Add(b,60)
    b.OnClick.Add(BtnRenameCallback)

def CreateTool():
    # Tool creation will serve as the hub for all other controls
    t = FBCreateUniqueTool("Find and Replace Take Names")
    t.StartSizeX = 300
    t.StartSizeY = 200

    PopulateLayout(t)
    ShowTool(t)
    
CreateTool()

##old_Name = "_"
##new_Name = " "
##
##name = old_Name
##
##name = name.replace(old_Name, new_Name)
##
##for take in lSys.Scene.Takes:
##    take.Name = take.Name.replace(old_Name, new_Name)
##    print take.Name
    