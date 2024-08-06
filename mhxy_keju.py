from mhxy import *

class Keju(MhxyScript):

    def find_keju(self):
        for _ in range(0, 3):
            kejuLocation = Util.locateCenterOnScreen('resources/keju/keju.png')
            if kejuLocation is not None:
                return kejuLocation
            cooldown(2)
            pyautogui.moveTo(winRelativeX(10), winRelativeY(10))
            pyautogui.dragTo(winRelativeX(10), winRelativeY(4.6), duration=0.8)


    def run_keju(self):
        self.open_huodong()
        cooldown(1)

        kejuLocation = self.find_keju()
        cooldown(2)
        print(f"===== run keju keju location:{kejuLocation}")
        if kejuLocation is None:
            return False
        pyautogui.leftClick(kejuLocation.x + relativeX2Act(4), kejuLocation.y + relativeY2Act(0.3))

        kejuDone = Util.locateOnScreen('resources/keju/keju_done.png')
        print(f"===== run keju keju done location:{kejuDone}")
        if kejuDone is not None:
            return False
        return True


    def do(self):
        if self.run_keju() is False:
            return
        while self._flag:
            kejuLocation = Util.locateCenterOnScreen('resources/keju/keju_qiuzhu.png')
            print(f"===== kejuLocation:{kejuLocation}")
            if kejuLocation is not None:
                pyautogui.leftClick(kejuLocation.x, kejuLocation.y - relativeY2Act(5))
                # pyautogui.leftClick(kejuLocation.left + kejuLocation.width - 50,
                #                     kejuLocation.top + kejuLocation.height - 20)
                print("开始答题", kejuLocation)
            cooldown(2)

            kejuScore = Util.locateOnScreen('resources/keju/keju_score.png')
            if kejuScore is None:
                print("答题结束")
                return


if __name__ == '__main__':
    Keju().do()
