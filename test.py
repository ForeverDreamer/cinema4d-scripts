import c4d

obj = c4d.BaseObject(c4d.Ocube) # Create new cube
obj.SetRelPos(c4d.Vector(20))   # Set position of cube
doc.InsertObject(obj)           # Insert object in document
c4d.EventAdd()
