"""
AR_F@#kUpNodes

Author: Arttu Rautio (aturtur)
Website: http://aturtur.com/
Name-US: AR_F@#kUpNodes
Version: 1.0.0
Description-US: Messes position of selected nodes (2023 April Fools' Day)

Notice: Make sure the Xpresso tag or the Redshift material is selected when using the script!

Written for Maxon Cinema 4D R25.010
Python version 3.9.1

Change log:
1.0.0 (01.04.2023) - Alt modifier: The rightmost node rules
"""

# Libraries
import c4d
import random
from operator import attrgetter
try:
    import redshift
except:
    pass

# Classes
class nodeObject(object):
    def __init__(self, obj, px, py, sx, sy):
        self.node = obj # Node object
        self.px = px # X position
        self.py = py # Y position
        self.sx = sx # X scale
        self.sy = sy # Y scale

# Functions
def GetKeyMod():
    bc = c4d.BaseContainer() # Initialize a base container
    keyMod = "None" # Initialize a keyboard modifier status
    if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD,c4d.BFM_INPUT_CHANNEL,bc):
        if bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QSHIFT:
            if bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QCTRL: # Ctrl + Shift
                if bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QALT: # Alt + Ctrl + Shift
                    keyMod = 'Alt+Ctrl+Shift'
                else: # Shift + Ctrl
                    keyMod = 'Ctrl+Shift'
            elif bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QALT: # Alt + Shift
                keyMod = 'Alt+Shift'
            else: # Shift
                keyMod = 'Shift'
        elif bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QCTRL:
            if bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QALT: # Alt + Ctrl
                keyMod = 'Alt+Ctrl'
            else: # Ctrl
                keyMod = 'Ctrl'
        elif bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QALT: # Alt
            keyMod = 'Alt'
        else: # No keyboard modifiers used
            keyMod = 'None'
        return keyMod

def MessUpTheNodes(nodeMaster, keyMod):
    nodes = [] # Initialize a list for collecting nodes
    root = nodeMaster.GetRoot() # Get xpresso root
    for node in root.GetChildren(): # Iterate through nodes
        if node.GetBit(c4d.BIT_ACTIVE): # If node is selected
            bc = node.GetData() # Get copy of base container
            bsc = bc.GetContainer(c4d.ID_SHAPECONTAINER) # Get copy of shape container
            bcd = bsc.GetContainer(c4d.ID_OPERATORCONTAINER) # Get copy of operator container
            px  = bcd.GetReal(100) # Get x position
            py  = bcd.GetReal(101) # Get y position
            sx  = bcd.GetReal(108) # Get x scale
            sy  = bcd.GetReal(109) # Get y scale
            nodes.append(nodeObject(node, px, py, sx, sy)) # Create nodeObject and add it to a list

    nodeMaster.AddUndo() # Add undo for changing nodes
    if nodes:
        minX = min(nodes, key=attrgetter('px'))
        maxX = max(nodes, key=attrgetter('px'))
        minY = min(nodes, key=attrgetter('py'))
        maxY = max(nodes, key=attrgetter('py'))

    for i in range(0, len(nodes)): # Iterate through collected nodes
        node =  nodes[i].node # Get node
        bc = node.GetDataInstance() # Get base container
        bsc = bc.GetContainerInstance(c4d.ID_SHAPECONTAINER) # Get shape container
        bcd = bsc.GetContainerInstance(c4d.ID_OPERATORCONTAINER) # Get operator container

        extra = 100

        py = random.randint(int(minY.py)-extra, int(maxY.py)+extra)
        px = random.randint(int(minX.px)-extra, int(maxX.px)+extra)

        bcd.SetReal(100, px) # Set x position
        bcd.SetReal(101, py) # Set y position

def main():
    doc = c4d.documents.GetActiveDocument() # Get active document
    bc = c4d.BaseContainer() # Initialize a base container
    keyMod = GetKeyMod() # Get keymodifier
    doc.StartUndo() # Start recording undos
    materials = doc.GetMaterials() # Get materials
    selection = doc.GetSelection() # Get active selection
    #try: # Try to execute following script
        # Xpresso
    for s in selection: # Iterate through selection
        if type(s).__name__ == "XPressoTag": # If operator is xpresso tag
            xpnm = s.GetNodeMaster() # Get node master
            MessUpTheNodes(xpnm, keyMod) # Run the main function
    # Redshift
    for m in materials: # Iterate through materials
        if m.GetBit(c4d.BIT_ACTIVE): # If material is selected
            rsnm = redshift.GetRSMaterialNodeMaster(m) # Get Redshift material node master
            MessUpTheNodes(rsnm, keyMod) # Run the main function
    #except: # Otherwise
    #    pass # Do nothing
    doc.EndUndo() # Stop recording undos
    c4d.EventAdd() # Refresh Cinema 4D

# Execute main()
if __name__=='__main__':
    main()