from pyfbsdk import *
    
app = FBApplication()
subStr = "Move"
lSys  = FBSystem()

def makeUniq(name):
    for take in lSys.Scene.Takes:
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
    app.FileMerge( lFilePath , False, lOptions )

def getFile():
    lFp = FBFilePopup()
    lFp.Caption = "Prop Menu Merge: Select a file"
    lFp.Style = FBFilePopupStyle.kFBFilePopupOpen
    ## options = FBFbxOptions(True)
    lFp.Filter = "*.fbx"
    lFp.Path = "C:\somethingsomething"
    lRes = lFp.Execute()
    lFilePath =lFp.FullFilename
    return lFilePath
    
def main():
    mergedFile  = getFile()
    merge(mergedFile, subStr)


if __name__ in ('__name__', '__builtin__'): 
    main()