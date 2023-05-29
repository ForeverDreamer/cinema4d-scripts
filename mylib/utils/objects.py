import c4d


def config_props(obj, props):
    for prop in props:
        if prop['type'] == 'Vector':
            prop['value'] = False
        elif prop['type'] == 'int':
            prop['value'] = 0
        elif prop['type'] == 'float':
            prop['value'] = 0.0
        else:
            obj[getattr(c4d, prop['k'])] = prop['v']


def create_object(conf):
    # 在UI界面把对象用鼠标拖进python consloe查看对象类型和属性
    obj = c4d.BaseObject(conf['_type'])  # Create new cube
    obj.SetRelPos(c4d.Vector(*conf['pos']))  # Set position of cube
    c4d.documents.GetActiveDocument().InsertObject(obj)  # Insert object in document
    c4d.EventAdd()
