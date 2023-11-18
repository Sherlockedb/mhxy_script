from mhxy import *

class Baotu(MhxyScript):

    def find_baotu(self):
        for _ in range(0, 3):
            baotuLocation = Util.locateCenterOnScreen('resources/baotu/baotu.png')
            if baotuLocation is not None:
                return baotuLocation
            cooldown(2)
            pyautogui.moveTo(winRelativeX(10), winRelativeY(10))
            pyautogui.dragTo(winRelativeX(10), winRelativeY(4.6), duration=0.8)

    def open_huodong(self):
        for i in range(0, 10):
            pyautogui.hotkey('alt', 'c')
            cooldown(1)
            print(f"===== try open huodong i:{i}")
            baotuLocation = Util.locateCenterOnScreen('resources/baotu/activity.png')
            if baotuLocation is not None:
                break

    def run_baotu(self, check_do=True):
        self.open_huodong()
        # cooldown(0.5)
        # pyautogui.hotkey('alt', 'c')
        # Util.leftClick(7.5, 1.5)
        cooldown(1)
        Util.leftClick(3, 4.5)
        cooldown(1)

        baotuLocation = self.find_baotu()
        cooldown(2)
        print(f"===== run baotu baotu location:{baotuLocation}")
        if baotuLocation is None:
            return False
        pyautogui.leftClick(baotuLocation.x + relativeX2Act(4), baotuLocation.y + relativeY2Act(0.3))

        baotuDone = Util.locateOnScreen('resources/baotu/baotu_done.png')
        print(f"===== run baotu baotu done location:{baotuDone}")
        if baotuDone is not None:
            return False

        if check_do is False:
            print("继续宝图")
            return True

        for _ in range(1, 30):
            cooldown(2)
            dobaotu = Util.locateOnScreen('resources/baotu/baotu_do.png')
            print(f"===== run baotu check do location:{baotuDone}")
            if dobaotu is not None:
                pyautogui.leftClick(dobaotu.left + dobaotu.width - 50,
                                    dobaotu.top + dobaotu.height - 20)
                print("开始宝图", dobaotu)
                cooldown(1)
                pyautogui.leftClick(dobaotu.left + dobaotu.width - 50,
                                    dobaotu.top + dobaotu.height - 20)
                cooldown(1)
                return self.run_baotu(check_do=False)

        return True


    def do(self):
        if self.run_baotu() is False:
            return
        i = 0
        while self._flag:
            cooldown(30)
            i += 1

            # 战斗标识
            battleLoc = Util.locateOnScreen('resources/small/enter_battle_flag.png')
            if battleLoc is not None:
                continue

            if i % 10 == 0: # 每5分钟检测下
                if self.run_baotu(check_do=False) is False:
                    return
                i = 0


if __name__ == '__main__':
    Baotu().do()
