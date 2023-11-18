from mhxy import *

class ClearUI(MhxyScript):

    def do(self):
        for _ in range(0, 10):
            pyautogui.rightClick(winRelativeX(10), winRelativeY(10))


if __name__ == '__main__':
    ClearUI().do()
