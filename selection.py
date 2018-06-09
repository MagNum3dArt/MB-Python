import pyfbsdk as sdk

def GetLast():
    selected_objects = sdk.FBModelList()
    sdk.FBGetSelectedModels(selected_objects, None, True, True)
    if len(selected_objects)>0:
        last_selected_object = selected_objects[-1]
        return last_selected_object
    else:
        sdk.FBMessageBox( "Warning:", "Nothing is selected!", "OK" )
        return