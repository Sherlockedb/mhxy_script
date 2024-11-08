from mhxy import *

from mhxy_baotu import *
from mhxy_yunbiao import *
from mhxy_shimen import *
from mhxy_sjqy import *
from mhxy_clear_ui import *
from mhxy_keju import *
from mhxy_bangpai2 import *
from mhxy_mjxy import *


class AutoTask(MhxyScript):

    def do(self):
        task_cls = [Shimen, Mjxy, Baotu, Sjqy, Keju, Yunbiao]
        clear_ui = ClearUI()

        for cls in task_cls:
            if not self._flag:
                break
            clear_ui.do()
            print("开始任务：", cls)
            task = cls()
            task._flag = self._flag
            task.do()


if __name__ == '__main__':
    AutoTask.do()
