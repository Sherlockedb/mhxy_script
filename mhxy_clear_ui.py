from mhxy import *

class ClearUI(MhxyScript):

    def try_close_item(self):
        items = [
            'resources/common/close_item.png',
            'resources/common/close_item2.png',
            'resources/common/close_item3.png',
            'resources/common/close_item4.png',
            'resources/common/close_item5.png',
            'resources/common/close_item6.png',
            'resources/common/close_item7.png',
        ]
        itemLocation = Util.locateCenterOnScreen(items)
        # print('close itemLocation:', itemLocation)
        if itemLocation is None:
            return

        pyautogui.leftClick(itemLocation.x, itemLocation.y)
        cooldown(1)

    def do(self):
        for _ in range(0, 5):
            self.try_close_item()


if __name__ == '__main__':
    ClearUI().do()
