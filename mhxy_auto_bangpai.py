import sys
from mhxy import *

class AutoBangpai(MhxyScript):

    # chaseWin = [-0.5, 3.8 + 0]

    # def __init__(self, idx=0, changWinPos=True) -> None:
    #     # init(resizeToSmall=True)
    #     super().__init__(idx=idx, changWinPos=changWinPos)

    def find_bangpai(self):
        for _ in range(0, 3):
            bangpaiLocation = Util.locateCenterOnScreen('resources/auto_bangpai/bangpai_task.png')
            if bangpaiLocation is not None:
                return bangpaiLocation
            cooldown(2)
            pyautogui.moveTo(winRelativeX(10), winRelativeY(10))
            pyautogui.dragTo(winRelativeX(10), winRelativeY(4.6), duration=0.8)


    def run_bangpai(self):
        self.open_huodong()
        cooldown(1)

        bangpaiLocation = self.find_bangpai()
        cooldown(2)
        print(f"===== run bangpai bangpai location:{bangpaiLocation}")
        if bangpaiLocation is None:
            return False
        pyautogui.leftClick(bangpaiLocation.x + relativeX2Act(4), bangpaiLocation.y + relativeY2Act(0.3))

        bangpaiDone = Util.locateOnScreen('resources/auto_bangpai/bangpai_task_done.png')
        print(f"===== run bangpai bangpai done location:{bangpaiDone}")
        if bangpaiDone is not None:
            return False
        return True

    def do(self):
        if self.run_bangpai() is False:
            return
        # pyautogui.leftClick(self.chaseWin[0], self.chaseWin[1])
        while True:
            locate = Util.locateCenterOnScreen('resources/auto_bangpai/bangpai_done.png')
            if locate is not None:
                again_locate = Util.locateCenterOnScreen('resources/auto_bangpai/bangpai_again.png')
                if again_locate is not None:
                    pyautogui.leftClick(again_locate.x, again_locate.y)
                else:
                    print("帮派任务结束")
                    return

            cooldown(4)


if __name__ == '__main__':
    idx = 0 if len(sys.argv) <= 1 else int(sys.argv[1])
    pyautogui.PAUSE = 0.5
    print("start task....")
    AutoBangpai(idx=idx).do()

