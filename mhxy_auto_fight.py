from mhxy import *

class AutoFight(MhxyScript):

    def do(self):
        while self._flag:
            autoLocation = Util.locateCenterOnScreen('resources/auto_fight/auto.png')
            if autoLocation is not None:
                cooldown(0.5)
                pyautogui.leftClick(autoLocation.x,
                                    autoLocation.y)
                print("开启自动战斗 ", autoLocation)
                i = 0
            cooldown(2)

        print("结束任务")


if __name__ == '__main__':
    AutoFight().do()
