####################################################################
##
## FnR_TakeRenamer.py
## Author Alexander <MagNum3D> Malin 2017
## 3.d@ukr.net
## www.nasna.ga
##
####################################################################
from pyfbsdk import *
from pyfbsdk_additions import *

# Creating all the Constructors
lSys = FBSystem()


editStyles = ["Find", "Replace", "Prefix", "Suffix"]

edits = {}

# Find Asterix in find and replace fields 
def FindAsterix(find, replace):
    
    asterix = "*"
    
    if find == asterix and asterix in replace:
        return True
        
    return False

# Find Errors    
def FindWarning(find, replace, prefix, suffix, asterix_in_find):
    
    selected = 0
    changed = 0 

    for take in lSys.Scene.Takes:
        if take.Selected:
                
            selected += 1
            old_name = take.Name
            # If there is Asterix - use whole take name
            new_name =( 
                replace.replace("*",take.Name) if asterix_in_find else 
                old_name.replace(find, replace)
                )
            # Add prefix and suffix
            new_name = prefix + new_name+ suffix
            if old_name != new_name:
                changed += 1

    if selected == 0:
        FBMessageBox( "Warning:", "There is no selected Takes!", "OK" )
        return True
    if find == '' and prefix == '' and suffix == '':
        FBMessageBox( "Warning:", "There is nothing to Find!", "OK" )
        return True
    if replace == find and prefix == '' and suffix == '':
        FBMessageBox( "Warning:", "Replace is the same as Find!", "OK" )
        return True
    if changed == 0:
        FBMessageBox( "Warning:", "There is no '%s' in selected takes" %find, "OK" )
        return True
        
    return False
     

# Callback of the button 'Rename'
def BtnRenameCallback(control,event):

    e = edits['Find']
    find = e.Text
    e = edits['Replace']
    replace = e.Text
    e = edits['Prefix']
    prefix = e.Text
    e = edits['Suffix']
    suffix = e.Text
    
    asterix_in_find = FindAsterix(find, replace)

    if FindWarning(find, replace, prefix, suffix, asterix_in_find):
        return

    for take in lSys.Scene.Takes:
        if take.Selected:
            # If there is Asterix - use whole take name
            take.Name =(
                replace.replace("*",take.Name) if asterix_in_find else 
                take.Name.replace(find, replace)
                )
            # Add prefix and suffix
            take.Name = prefix + take.Name + suffix

    FBMessageBox( "Changes:",  "Takes are renamed", "OK" )
        

    
def PopulateLayout(mainLyt):
    
    anchor = ""
    attachType = FBAttachType.kFBAttachTop

    # Create different fields
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
            
        # Create field
        editId = "Edit" + style
        initCall = "%s()" % ("FBEdit")
        e = eval( initCall )
        e.Text = ""
        edits[style] = e
        
        
        x = FBAddRegionParam(10,FBAttachType.kFBAttachRight,labId)
        y = FBAddRegionParam(10,attachType,anchor)
        w = FBAddRegionParam(200,FBAttachType.kFBAttachNone,"")
        h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
    
        mainLyt.AddRegion(editId,editId, x, y, w, h)
    
        mainLyt.SetControl(editId,e)
      
        attachType = FBAttachType.kFBAttachBottom
        anchor = labId
        
    
    # Add button 
    btn_width = 100
    x = FBAddRegionParam(-btn_width-5,FBAttachType.kFBAttachRight,editId)
    y = FBAddRegionParam(10,attachType,anchor)
    w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
    h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
    mainLyt.AddRegion("main","main", x, y, w, h)
    lyt = FBHBoxLayout()
    mainLyt.SetControl("main",lyt)
    
    
    b = FBButton()
    b.Caption = "Rename"
    b.Justify = FBTextJustify.kFBTextJustifyCenter
    lyt.Add(b,btn_width)
    b.OnClick.Add(BtnRenameCallback)

def CreateTool():
    # Tool creation will serve as the hub for all other controls
    t = FBCreateUniqueTool("Find and Replace Take Names")
    t.StartSizeX = 300
    t.StartSizeY = 210

    PopulateLayout(t)
    ShowTool(t)
    
if __name__ in ('__name__', '__builtin__'):
    CreateTool()
