from mhxy import *

class Sjqy(MhxyScript):

    def find_sjqy(self):
        for _ in range(0, 3):
            sjqyLocation = Util.locateCenterOnScreen('resources/sjqy/sjqy.png')
            if sjqyLocation is not None:
                return sjqyLocation
            cooldown(2)
            pyautogui.moveTo(winRelativeX(10), winRelativeY(10))
            pyautogui.dragTo(winRelativeX(10), winRelativeY(4.6), duration=0.8)


    def run_sjqy(self):
        Util.leftClick(7.5, 1.5)
        cooldown(1)
        Util.leftClick(3, 4.5)
        cooldown(1)

        sjqyLocation = self.find_sjqy()
        cooldown(2)
        print(f"===== run sjqy sjqy location:{sjqyLocation}")
        if sjqyLocation is None:
            return False
        pyautogui.leftClick(sjqyLocation.x + relativeX2Act(4), sjqyLocation.y + relativeY2Act(0.3))

        sjqyDone = Util.locateOnScreen('resources/sjqy/sjqy_done.png')
        print(f"===== run sjqy sjqy done location:{sjqyDone}")
        if sjqyDone is not None:
            return False
        return True


    def do(self):
        if self.run_sjqy() is False:
            return
        while self._flag:
            sjqyLocation = Util.locateCenterOnScreen('resources/sjqy/sjqy_qiuzhu.png')
            print(f"===== sjqyLocation:{sjqyLocation}")
            if sjqyLocation is not None:
                pyautogui.leftClick(sjqyLocation.x, sjqyLocation.y - relativeY2Act(2))
                # pyautogui.leftClick(sjqyLocation.left + sjqyLocation.width - 50,
                #                     sjqyLocation.top + sjqyLocation.height - 20)
                print("开始答题", sjqyLocation)
            cooldown(2)

            sjqyFinish = Util.locateOnScreen('resources/sjqy/sjqy_finish.png')
            if sjqyFinish is not None:
                print("答题结束", sjqyFinish)
                return


if __name__ == '__main__':
    Sjqy().do()
