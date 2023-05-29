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

splinetextObj = c4d.BaseObject(c4d.Osplinetext)  # Create new cube
extrudeObj = c4d.BaseObject(c4d.Oextrude)
extrudeObj[getattr(c4d, 'EXTRUDEOBJECT_EXTRUSIONOFFSET')] = 20
extrudeObj[c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_X]
c4d.documents.GetActiveDocument().InsertObject(extrudeObj)  # Insert object in document
c4d.documents.GetActiveDocument().InsertObject(splinetextObj, extrudeObj)
c4d.EventAdd()