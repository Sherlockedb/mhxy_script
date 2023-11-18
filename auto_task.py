from mhxy_baotu import *
from mhxy_yunbiao import *
from mhxy_shimen import *
from mhxy_sjqy import *
from mhxy_clear_ui import *
from mhxy_keju import *
from mhxy_bangpai2 import *

def auto_do_task():
    clear_ui = ClearUI()

    clear_ui.do()
    Shimen().do()

    clear_ui.do()
    Baotu().do()

    clear_ui.do()
    Sjqy().do()

    clear_ui.do()
    Yunbiao().do()

    clear_ui.do()
    Keju().do()


if __name__ == '__main__':
    auto_do_task()
