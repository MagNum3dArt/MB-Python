import pyfbsdk as sdk
import mgnLib.long_name as ln

def Get(model = None):
    if model:
        name_spaces_list = ln.Split(model.LongName)
        del(name_spaces_list[-1])
        colon = ':'
        name_space = colon.join(name_spaces_list)
        return name_space
    else:
        sdk.FBMessageBox( "Warning:", "There is NO object to get it's Name Space!", "OK" )
        return
