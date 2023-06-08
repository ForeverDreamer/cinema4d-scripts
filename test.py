import os
import sys
from pprint import pprint as pp

import c4d
from dotenv import load_dotenv

from mylib.utils import *


load_dotenv()

share.init()

# for conf in [
#     {'_type': c4d.Ocube, 'pos': [0, 100, 0]},
#     {'_type': c4d.Ocylinder, 'pos': [0, 100, 200]},
#     {'_type': c4d.Ocone, 'pos': [0, 100, 400]},
# ]:
#     objects.create_object(conf)
#
# doc = c4d.documents.GetActiveDocument()
# objs = doc.GetObjects()
# for obj in objs:
#     print(obj)
# pp(objs)

floorObj = c4d.BaseObject(c4d.Ofloor)
floorObj[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(0, -60, 0)
splinetextObj = c4d.BaseObject(c4d.Osplinetext)
splinetextObj[c4d.PRIM_TEXT_TEXT] = 'Python'
extrudeObj = c4d.BaseObject(c4d.Oextrude)
lightObj_1 = c4d.BaseObject(c4d.Olight)
lightObj_1[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(100, 500, -300)
lightObj_1[c4d.ID_BASEOBJECT_REL_ROTATION] = c4d.Vector(-45, -30, 0)

lightObj_2 = c4d.BaseObject(c4d.Olight)
lightObj_2[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(600, 200, -300)
lightObj_2[c4d.ID_BASEOBJECT_REL_ROTATION] = c4d.Vector(45, 30, 0)
lightObj_2[c4d.LIGHT_BRIGHTNESS] = 0.7

lightObj_3 = c4d.BaseObject(c4d.Olight)
lightObj_3[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(600, 200, 100)
lightObj_3[c4d.ID_BASEOBJECT_REL_ROTATION] = c4d.Vector(180, 0, 0)
lightObj_3[c4d.LIGHT_BRIGHTNESS] = 0.3

extrudeObj[getattr(c4d, 'EXTRUDEOBJECT_EXTRUSIONOFFSET')] = 20
# extrudeObj[c4d.ID_BASEOBJECT_USECOLOR] = 2
# extrudeObj[c4d.ID_BASEOBJECT_COLOR] = c4d.Vector(0.164, 0.744, 0.821)
extrudeObj[c4d.CAPSANDBEVELS_STARTBEVEL_OFFSET] = 3
extrudeObj[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(0, 100, 0)
# extrudeObj[c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_X]

doc = c4d.documents.GetActiveDocument()
doc.InsertObject(floorObj)
doc.InsertObject(extrudeObj)
doc.InsertObject(splinetextObj, extrudeObj)
doc.InsertObject(lightObj_1)
doc.InsertObject(lightObj_2)
doc.InsertObject(lightObj_3)

mat = c4d.Material()
mat.SetChannelState(c4d.CHANNEL_COLOR, True)
mat[c4d.MATERIAL_COLOR_COLOR] = c4d.Vector(0.164, 0.744, 0.821)
shader = c4d.BaseShader(c4d.Xearth)
mat.InsertShader(shader)
mat[c4d.MATERIAL_COLOR_SHADER] = shader
mat.Message(c4d.MSG_UPDATE)
mat.Update(True, True)
for i in range(3):
    refLayer = mat.AddReflectionLayer()
    refLayer.SetName('MyLayer'+str(i))
    mat[refLayer.GetDataID() + c4d.REFLECTION_LAYER_MAIN_DISTRIBUTION] = c4d.REFLECTION_DISTRIBUTION_LAMBERTIAN
# matlist = doc.GetMaterials()
doc.InsertMaterial(mat)
# mat = doc.SearchMaterial(matName)
tag = extrudeObj.MakeTag(c4d.Ttexture)
tag[c4d.TEXTURETAG_MATERIAL] = mat
c4d.EventAdd()
