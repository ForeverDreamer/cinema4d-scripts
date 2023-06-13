import c4d
from dotenv import load_dotenv

from mylib.utils import *


load_dotenv()

share.init()


# Welcome to the world of Python
def add_key(obj, conf):
    doc = c4d.documents.GetActiveDocument()

    # Creates the track in memory. Defined by it's DESCID
    desc_levels = []
    for attrs in conf['desc_levels']:
        attrs = [getattr(c4d, attr) for attr in attrs]
        if len(attrs) == 2:
            attrs.append(0)
        desc_levels.append(c4d.DescLevel(*attrs))
    tr = c4d.CTrack(
        obj,
        c4d.DescID(*desc_levels)
    )
    # Gets Curves for the track
    curve = tr.GetCurve()

    for key in conf['keys']:
        key_time = c4d.BaseTime(key[0], doc.GetFps())
        added = curve.AddKey(key_time)
        if added is None:
            raise TypeError("cannont create a key")
        key_obj = added["key"]
        nidx = added["nidx"]
        key_obj.SetValue(curve, key[1])
        key_obj.SetInterpolation(curve, c4d.CINTERPOLATION_SPLINE)
        curve.SetKeyDefault(doc, nidx)

    # Inserts track to the object
    obj.InsertTrackSorted(tr)
    # Inserts the object in document
    doc.InsertObject(obj)
    # Pushes an update event to Cinema 4D
    c4d.EventAdd()


# Main function
def main():
    # Creates the object in memory
    obj = c4d.BaseObject(c4d.Ocube)

    conf_y = {
        'desc_levels': [
            ['ID_BASEOBJECT_POSITION', 'DTYPE_VECTOR'],
            ['VECTOR_Y', 'DTYPE_REAL']
        ],
        'keys': [(0, 0), (10, 100), (20, 100), (30, 200), (40, 200), (50, 300)]
    }
    add_key(obj, conf_y)
    conf_x = {
        'desc_levels': [
            ['ID_BASEOBJECT_POSITION', 'DTYPE_VECTOR'],
            ['VECTOR_X', 'DTYPE_REAL']
        ],
        'keys': [(0, 0), (10, 100), (20, 100), (30, 200), (40, 200), (50, 300)]
    }
    add_key(obj, conf_x)


# Execute main()
if __name__ == '__main__':
    main()
