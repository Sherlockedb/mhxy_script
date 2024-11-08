from mhxy import *

class Shimen(MhxyScript):

    def find_shimen(self):
        for _ in range(0, 3):
            shimenLocation = Util.locateCenterOnScreen('resources/shimen/shimen.png')
            if shimenLocation is not None:
                return shimenLocation
            cooldown(2)
            pyautogui.moveTo(winRelativeX(10), winRelativeY(10))
            pyautogui.dragTo(winRelativeX(10), winRelativeY(4.6), duration=0.8)


    def run_shimen(self):
        self.open_huodong()
        cooldown(1)

        shimenLocation = self.find_shimen()
        cooldown(2)
        print(f"===== run shimen shimen location:{shimenLocation}")
        if shimenLocation is None:
            return False
        pyautogui.leftClick(shimenLocation.x + relativeX2Act(4), shimenLocation.y + relativeY2Act(0.3))

        shimenDone = Util.locateOnScreen('resources/shimen/shimen_done.png')
        print(f"===== run shimen shimen done location:{shimenDone}")
        if shimenDone is not None:
            return False

        cooldown(0.5)
        doShimen = Util.locateOnScreen('resources/shimen/shimen_do.png')
        if doShimen is not None:
            pyautogui.leftClick(doShimen.left + doShimen.width - 50,
                                doShimen.top + doShimen.height - 20)
            print("开始做师门 ", doShimen)
            return True

        cooldown(0.5)
        doShimen = Util.locateOnScreen('resources/shimen/shimen_continue.png')
        if doShimen is not None:
            pyautogui.leftClick(doShimen.left + doShimen.width - 50,
                                doShimen.top + doShimen.height - 20)
            print("继续做师门 ", doShimen)
            return True

        return False


    def do(self):
        if self.run_shimen() is False:
            return
        i = 0
        while self._flag:
            shimenLocation = Util.locateOnScreen('resources/shimen/shimen_finish.png')
            print(f"===== shimenLocation:{shimenLocation}")
            if shimenLocation is not None:
                return
            cooldown(10)
            shimenTaskLocation = Util.locateCenterOnScreen('resources/shimen/shimen_task.png')
            if shimenTaskLocation is not None:
                pyautogui.leftClick(shimenTaskLocation.x, shimenTaskLocation.y)
            cooldown(20)
            i += 1
            if i % 10 == 0: # 5分钟没师门了，再检测一下
                if self.run_shimen() is False:
                    return
                i = 0


if __name__ == '__main__':
    Shimen().do()
