import pyfbsdk as sdk
import mgnLib.long_name as ln; reload(ln)

def Get(model = None):
    if model:
        name = ln.Split(model.LongName)[-1]
        return name
    else:
        sdk.FBMessageBox( "Warning:", "There is NO object to get it's Name!", "OK" )
        return