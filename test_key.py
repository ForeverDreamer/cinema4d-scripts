import c4d


# Welcome to the world of Python


# Main function
def main():
    doc = c4d.documents.GetActiveDocument()
    # Creates the object in memory
    obj = c4d.BaseObject(c4d.Ocube)

    # Creates the track in memory. Defined by it's DESCID
    trY = c4d.CTrack(
        obj,
        c4d.DescID(
            c4d.DescLevel(c4d.ID_BASEOBJECT_POSITION, c4d.DTYPE_VECTOR, 0),
            c4d.DescLevel(c4d.VECTOR_Y, c4d.DTYPE_REAL, 0)
        )
    )

    # Gets Curves for the track
    curveY = trY.GetCurve()

    # Retrieves the current time
    keyTime = c4d.BaseTime(0)

    # Adds the keys
    added = curveY.AddKey(keyTime)

    # Checks for error
    if added is None:
        raise TypeError("cannont create a key")

    # Retrieves the inserted key
    firstKey = added["key"]
    kIndex = added["nidx"]

    # Sets the value of the key
    firstKey.SetValue(curveY, 0)

    # Changes it's interpolation
    firstKey.SetInterpolation(curveY, c4d.CINTERPOLATION_SPLINE)

    # Sets the key to default status AutoTangent etc...
    curveY.SetKeyDefault(doc, kIndex)

    # Adds another key
    keyTime = c4d.BaseTime(10, doc.GetFps())
    added = curveY.AddKey(keyTime)
    if added is None:
        raise TypeError("cannont create a key")
    secondKey = added["key"]
    kIndex = added["nidx"]
    secondKey.SetValue(curveY, 100)
    secondKey.SetInterpolation(curveY, c4d.CINTERPOLATION_SPLINE)
    curveY.SetKeyDefault(doc, kIndex)

    # Inserts track to the object
    obj.InsertTrackSorted(trY)

    # Inserts the object in document
    doc.InsertObject(obj)

    # Pushes an update event to Cinema 4D
    c4d.EventAdd()


# Execute main()
if __name__ == '__main__':
    main()