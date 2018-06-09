from pyfbsdk import *
from pyfbsdk_additions import *

def BtnSimpleCallback(control, event):
    
    marker = FBModelMarker('m_root')
    
    root = FBFindModelByLabelName('Root')
    root.Name = 'root'
    lMgr = FBConstraintManager()
    lCnst = lMgr.TypeCreateConstraint(5)
    lCnst.ReferenceAdd (0,marker)
    lCnst.ReferenceAdd (1,root)
    lCnst.Snap()
    lCnst.Active = True
    
    
    marker.Selected = True
    
    plotOptions = FBPlotOptions()
    plotOptions.ConstantKeyReducerKeepOneKey=False
    plotOptions.UseConstantKeyReducer = False
    plotOptions.PlotAllTakes = True
    plotOptions.PlotOnFrame  = True
    plotOptions.PlotPeriod   = FBTime( 0, 0, 0, 1 )
    
    
    FBSystem().CurrentTake.PlotTakeOnSelected( plotOptions )
    
    marker.Selected = False
    
    lCnst.Active = False
    
    lCnst.FBDelete()
    
    lCnst = lMgr.TypeCreateConstraint(5)
    lCnst.ReferenceAdd (0,root)
    lCnst.ReferenceAdd (1,marker)
    lCnst.Snap()
    lCnst.Active = True
    
    garbage = FBFindModelByLabelName('BaseNode')
    
    garbage.FBDelete()
    
    root.Selected = True
    
    FBSystem().CurrentTake.PlotTakeOnSelected( plotOptions )
    
    root.Selected = False
    
    lCnst.Active = False
    
    lCnst.FBDelete()
    
    marker.FBDelete()

def BtnCallback(control, event):
    marker = FBModelMarker('m_root')
    
    root = FBFindModelByLabelName('Root')
    root.Name = 'root'
    lMgr = FBConstraintManager()
    lCnst = lMgr.TypeCreateConstraint(3)
    lCnst.ReferenceAdd (0,marker)
    lCnst.ReferenceAdd (1,root)
    lCnst.Snap()
    lCnst.Active = True
    
    
    marker.Selected = True
    
    plotOptions = FBPlotOptions()
    plotOptions.ConstantKeyReducerKeepOneKey=False
    plotOptions.UseConstantKeyReducer = False
    plotOptions.PlotAllTakes = True
    plotOptions.PlotOnFrame  = True
    plotOptions.PlotPeriod   = FBTime( 0, 0, 0, 1 )
    
    
    FBSystem().CurrentTake.PlotTakeOnSelected( plotOptions )
    
    marker.Selected = False
    
    lCnst.Active = False
    
    lCnst.FBDelete()
    
    lCnst = lMgr.TypeCreateConstraint(3)
    lCnst.ReferenceAdd (0,root)
    lCnst.ReferenceAdd (1,marker)
    lCnst.Snap()
    lCnst.Active = True
    
    garbage = FBFindModelByLabelName('BaseNode')
    
    garbage.FBDelete()
    
    root.PropertyList.Find('RotationActive').Data = True
    # Get the prerotation handle
    lProp = root.PropertyList.Find( 'PreRotation' )

# Make a new vector
    lV3d = FBVector3d(-90,0,0)

    lProp.Data = lV3d

    
    root.Selected = True
    
    FBSystem().CurrentTake.PlotTakeOnSelected( plotOptions )
    
    root.Selected = False
    
    lCnst.Active = False
    
    lCnst.FBDelete()
    
    marker.FBDelete()
    
def PopulateLayout(mainLyt):
    x = FBAddRegionParam(100,FBAttachType.kFBAttachLeft,"")
    y = FBAddRegionParam(50,FBAttachType.kFBAttachTop,"")
    w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
    h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
    mainLyt.AddRegion("main","main", x, y, w, h)
    lyt = FBHBoxLayout()
    mainLyt.SetControl("main",lyt)

    b = FBButton()
    b.Caption = "Simple"
    b.Style = FBButtonStyle.kFB2States
    b.Look = FBButtonLook.kFBLookColorChange
    b.Justify = FBTextJustify.kFBTextJustifyCenter
    b.SetStateColor(FBButtonState.kFBButtonState0,FBColor(1.0, 0.0, 0.5))
    b.SetStateColor(FBButtonState.kFBButtonState1,FBColor(0.0, 1.0, 0.5))
    lyt.Add(b,60)
    
    b.OnClick.Add(BtnSimpleCallback)

    b = FBButton()
    b.Caption = "Complex"
    b.Style = FBButtonStyle.kFB2States
    b.Look = FBButtonLook.kFBLookColorChange
    b.Justify = FBTextJustify.kFBTextJustifyCenter
    b.SetStateColor(FBButtonState.kFBButtonState0,FBColor(1.0, 0.0, 0.5))
    b.SetStateColor(FBButtonState.kFBButtonState1,FBColor(0.0, 1.0, 0.5))
    lyt.Add(b,60)
    
    b.OnClick.Add(BtnCallback)
    
def CreateTool():
    # Tool creation will serve as the hub for all other controls
    t = FBCreateUniqueTool("Unreal2MB")
    t.StartSizeX = 400
    t.StartSizeY = 200
    PopulateLayout(t)
    ShowTool(t)
    

CreateTool()
