import os
import sys
from pprint import pprint as pp

import c4d
from dotenv import load_dotenv

load_dotenv()

from mylib.utils import *

if not os.environ.get('PYCHARM_ENV'):
    import importlib
    modules = [module for name, module in sys.modules.items() if name.startswith('mylib.')]
    for module in modules:
        importlib.reload(module)
    share.flush()

# share.restart_me()

for conf in [
    {'_type': c4d.Ocube, 'pos': [0, 100, 0]},
    {'_type': c4d.Ocylinder, 'pos': [0, 100, 200]},
    {'_type': c4d.Ocone, 'pos': [0, 100, 400]},
]:
    objects.create_object(conf)

doc = c4d.documents.GetActiveDocument()
objs = doc.GetObjects()
pp(objs)