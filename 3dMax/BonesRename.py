from pyfbsdk import *

bones = {

# Main bones
    'Bip01':            'Pelvis',
    'Bip01-Spine':      'spine_01',
    'Bip01-Spine1':     'spine_02',
    'Bip01-Spine2':     'spine_03',
    'Bip01-L-Clavicle': 'clavicle_l',
    'Bip01-L-UpperArm': 'upperarm_l',
    'Bip01-L-Forearm':  'lowerarm_l',
    'Bip01-L-Hand':     'hand_l',
    'Bip01-R-Clavicle': 'clavicle_r',
    'Bip01-R-UpperArm': 'upperarm_r',
    'Bip01-R-Forearm':  'lowerarm_r',
    'Bip01-R-Hand':     'hand_r',
    'Bip01-Neck':       'neck_01',
    'Bip01-Head':       'head',
    'Bip01-L-Thigh':    'thigh_l',
    'Bip01-L-Calf':     'calf_l',
    'Bip01-L-Foot':     'foot_l',
    'Bip01-R-Thigh':    'thigh_r',
    'Bip01-R-Calf':     'calf_r',
    'Bip01-R-Foot':     'foot_r',
# Extra bones
    'Bip01-L-Finger1': 'index_01_l',	
    'Bip01-L-Finger11': 'index_02_l',	
    'Bip01-L-Finger12': 'index_03_l',	
    'Bip01-L-Finger2': 'middle_01_l',	
    'Bip01-L-Finger21': 'middle_02_l',	
    'Bip01-L-Finger22': 'middle_03_l',	
    'Bip01-L-Finger4': 'pinky_01_l',	
    'Bip01-L-Finger41': 'pinky_02_l',	
    'Bip01-L-Finger42': 'pinky_03_l',	
    'Bip01-L-Finger3': 'ring_01_l',
    'Bip01-L-Finger31': 'ring_02_l',
    'Bip01-L-Finger32': 'ring_03_l',	
    'Bip01-L-Finger0': 'thumb_01_l',	
    'Bip01-L-Finger01': 'thumb_02_l',	
    'Bip01-L-Finger02': 'thumb_03_l',	
    'Bip01-L-ForeTwist': 'lowerarm_twist_01_l',	
    'Bip01-L-UpArmTwist': 'upperarm_twist_01_l',	
    'Bip01-R-Finger1': 'index_01_r',
    'Bip01-R-Finger11': 'index_02_r',
    'Bip01-R-Finger12': 'index_03_r',
    'Bip01-R-Finger2': 'middle_01_r',
    'Bip01-R-Finger21': 'middle_02_r',	
    'Bip01-R-Finger22': 'middle_03_r',	
    'Bip01-R-Finger4': 'pinky_01_r',	
    'Bip01-R-Finger41': 'pinky_02_r',	
    'Bip01-R-Finger42': 'pinky_03_r',	
    'Bip01-R-Finger3': 'ring_01_r',
    'Bip01-R-Finger31': 'ring_02_r',
    'Bip01-R-Finger32': 'ring_03_r',
    'Bip01-R-Finger0': 'thumb_01_r',	
    'Bip01-R-Finger01': 'thumb_02_r',	
    'Bip01-R-Finger02': 'thumb_03_r',	
    'Bip01-R-ForeTwist': 'lowerarm_twist_01_r',	
    'Bip01-R-UpArmTwist': 'upperarm_twist_01_r',
    'Bip01-L-Toe0': 'ball_l',
    'Bip01-R-Toe0': 'ball_r'

}

for key, value in bones.items(): # returns the dictionary as a list of value pairs -- a tuple.
    print key, value
    bone = FBFindModelByLabelName(key)
    if bone:
        bone.Name = value