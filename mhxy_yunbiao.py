from mhxy import *

class Yunbiao(MhxyScript):

    def find_yunbiao(self):
        for _ in range(0, 3):
            yunbiaoLocation = Util.locateCenterOnScreen('resources/yunbiao/yunbiao.png')
            if yunbiaoLocation is not None:
                return yunbiaoLocation
            cooldown(2)
            pyautogui.moveTo(winRelativeX(10), winRelativeY(10))
            pyautogui.dragTo(winRelativeX(10), winRelativeY(4.6), duration=0.8)


    def run_yunbiao(self):
        Util.leftClick(7.5, 1.5)
        cooldown(0.5)
        Util.leftClick(3, 4.5)
        cooldown(1)

        yunbiaoLocation = self.find_yunbiao()
        cooldown(2)
        if yunbiaoLocation is None:
            return False
        pyautogui.leftClick(yunbiaoLocation.x + relativeX2Act(4), yunbiaoLocation.y + relativeY2Act(0.3))

        yunbiaoDone = Util.locateOnScreen('resources/yunbiao/yunbiao_done.png')
        if yunbiaoDone is not None:
            return False

        return True


    def do(self):
        if self.run_yunbiao() is False:
            return
        i = 0
        while self._flag:
            yunbiaoLocation = Util.locateOnScreen('resources/yunbiao/putong_biaoyin.png')
            if yunbiaoLocation is not None:
                cooldown(0.5)
                pyautogui.leftClick(yunbiaoLocation.left + yunbiaoLocation.width - 50,
                                    yunbiaoLocation.top + yunbiaoLocation.height - 20)

                cooldown(0.5)
                yunbiaoConfirm = Util.locateOnScreen('resources/yunbiao/yunbiao_confirm.png')
                if yunbiaoConfirm is not None:
                    pyautogui.leftClick(yunbiaoConfirm.left + yunbiaoLocation.width - 50,
                                        yunbiaoConfirm.top + yunbiaoLocation.height - 20)
                    print("运镖中 ", yunbiaoLocation)
                    i = 0
            cooldown(30)
            i += 1
            if i % 10 == 0: # 5分钟没运镖了，再检测一下
                if self.run_yunbiao() is False:
                    return
                i = 0


if __name__ == '__main__':
    Yunbiao().do()
