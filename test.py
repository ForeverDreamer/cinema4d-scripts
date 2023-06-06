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
lightObj_1[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(100, 200, -300)
lightObj_1[c4d.ID_BASEOBJECT_REL_ROTATION] = c4d.Vector(-45, 0, 0)

lightObj_2 = c4d.BaseObject(c4d.Olight)
lightObj_2[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(600, 200, -300)
lightObj_2[c4d.ID_BASEOBJECT_REL_ROTATION] = c4d.Vector(45, 0, 0)
lightObj_2[c4d.LIGHT_BRIGHTNESS] = 0.7

lightObj_3 = c4d.BaseObject(c4d.Olight)
lightObj_3[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(600, 200, 100)
lightObj_3[c4d.ID_BASEOBJECT_REL_ROTATION] = c4d.Vector(180, 0, 0)
lightObj_3[c4d.LIGHT_BRIGHTNESS] = 0.3

extrudeObj[getattr(c4d, 'EXTRUDEOBJECT_EXTRUSIONOFFSET')] = 20
extrudeObj[c4d.ID_BASEOBJECT_USECOLOR] = 2
extrudeObj[c4d.ID_BASEOBJECT_COLOR] = c4d.Vector(0.164, 0.744, 0.821)
extrudeObj[c4d.CAPSANDBEVELS_STARTBEVEL_OFFSET] = 3
extrudeObj[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(0, 100, 0)
# extrudeObj[c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_X]

c4d.documents.GetActiveDocument().InsertObject(floorObj)
c4d.documents.GetActiveDocument().InsertObject(extrudeObj)
c4d.documents.GetActiveDocument().InsertObject(splinetextObj, extrudeObj)
c4d.documents.GetActiveDocument().InsertObject(lightObj_1)
c4d.documents.GetActiveDocument().InsertObject(lightObj_2)
c4d.documents.GetActiveDocument().InsertObject(lightObj_3)
c4d.EventAdd()
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
lightObj_1[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(100, 300, -300)
lightObj_1[c4d.ID_BASEOBJECT_REL_ROTATION] = c4d.Vector(-45, 0, 0)

lightObj_2 = c4d.BaseObject(c4d.Olight)
lightObj_2[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(600, 300, -300)
lightObj_2[c4d.ID_BASEOBJECT_REL_ROTATION] = c4d.Vector(45, 0, 0)
lightObj_2[c4d.LIGHT_BRIGHTNESS] = 0.7

lightObj_3 = c4d.BaseObject(c4d.Olight)
lightObj_3[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(600, 300, 100)
lightObj_3[c4d.ID_BASEOBJECT_REL_ROTATION] = c4d.Vector(180, 0, 0)
lightObj_3[c4d.LIGHT_BRIGHTNESS] = 0.3

extrudeObj[getattr(c4d, 'EXTRUDEOBJECT_EXTRUSIONOFFSET')] = 20
extrudeObj[c4d.ID_BASEOBJECT_USECOLOR] = 2
extrudeObj[c4d.ID_BASEOBJECT_COLOR] = c4d.Vector(0.164, 0.744, 0.821)
extrudeObj[c4d.CAPSANDBEVELS_STARTBEVEL_OFFSET] = 3
extrudeObj[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(0, 100, 0)
# extrudeObj[c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_X]

c4d.documents.GetActiveDocument().InsertObject(floorObj)
c4d.documents.GetActiveDocument().InsertObject(extrudeObj)
c4d.documents.GetActiveDocument().InsertObject(splinetextObj, extrudeObj)
c4d.documents.GetActiveDocument().InsertObject(lightObj_1)
c4d.documents.GetActiveDocument().InsertObject(lightObj_2)
c4d.documents.GetActiveDocument().InsertObject(lightObj_3)
c4d.EventAdd()
