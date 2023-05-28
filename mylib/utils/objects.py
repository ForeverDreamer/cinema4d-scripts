import c4d


def create_object(conf):
    obj = c4d.BaseObject(conf['_type'])  # Create new cube
    obj.SetRelPos(c4d.Vector(*conf['pos']))  # Set position of cube
    c4d.documents.GetActiveDocument().InsertObject(obj)  # Insert object in document
    c4d.EventAdd()
