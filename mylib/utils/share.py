import os
import sys

import c4d


# 第三方库需要拷贝到这两个目录的其中一个
# 'C:\Users\micro\AppData\Roaming\Maxon\Maxon Cinema 4D R25_63FF7547_p\python39\libs'
# 'C:\Users\micro\AppData\Roaming\Maxon\python\python39\libs'
def restart_me():
    c4d.RestartMe()


def flush():
    c4d.documents.GetActiveDocument().Flush()


def init():
    if not os.environ.get('PYCHARM_ENV'):
        import importlib
        modules = [module for name, module in sys.modules.items() if name.startswith('mylib.')]
        for module in modules:
            importlib.reload(module)
        flush()
