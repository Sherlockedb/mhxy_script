from mhxy import *

class Mjxy(MhxyScript):

    def find_mjxy(self):
        for _ in range(0, 3):
            mjxyLocation = Util.locateCenterOnScreen('resources/mjxy/mjxy.png')
            if mjxyLocation is not None:
                return mjxyLocation
            cooldown(2)
            pyautogui.moveTo(winRelativeX(10), winRelativeY(10))
            pyautogui.dragTo(winRelativeX(10), winRelativeY(4.6), duration=0.8)


    def run_mjxy(self):
        self.open_huodong()
        cooldown(1)

        mjxyLocation = self.find_mjxy()
        cooldown(2)
        print(f"===== run mjxy mjxy location:{mjxyLocation}")
        if mjxyLocation is None:
            return False
        pyautogui.leftClick(mjxyLocation.x + relativeX2Act(4), mjxyLocation.y + relativeY2Act(0.3))

        mjxyDone = Util.locateOnScreen('resources/mjxy/mjxy_done.png')
        print(f"===== run mjxy mjxy done location:{mjxyDone}")
        if mjxyDone is not None:
            return False

        for _ in range(1, 10):
            cooldown(2)
            mjxyOpt = Util.locateOnScreen('resources/mjxy/mjxy_opt.png')
            print(f"===== run mjxyOpt check do location:{mjxyOpt}")
            if mjxyOpt is not None:
                pyautogui.leftClick(mjxyOpt.left + mjxyOpt.width - 50,
                                    mjxyOpt.top + mjxyOpt.height - 20)
                cooldown(2)

                mjxyYcxz = Util.locateCenterOnScreen('resources/mjxy/mjxy_ycxz.png')
                if mjxyYcxz is None:
                    mjxyYcxz = Util.locateCenterOnScreen('resources/mjxy/mjxy_hdmj.png')
                if mjxyYcxz is not None:
                    pyautogui.leftClick(mjxyYcxz.x, mjxyYcxz.y + relativeY2Act(10))
                    cooldown(2)
                    mjxyConfirm = Util.locateCenterOnScreen('resources/mjxy/mjxy_confirm.png')
                    if mjxyConfirm is not None:
                        pyautogui.leftClick(mjxyConfirm.x, mjxyConfirm.y)
                        print("选择秘境", mjxyYcxz)
                        cooldown(2)

                mjxy_challenge = Util.locateOnScreen('resources/mjxy/mjxy_challenge.png')
                if mjxy_challenge is not None:
                    pyautogui.leftClick(mjxy_challenge.left + mjxy_challenge.width - 50,
                                        mjxy_challenge.top + mjxy_challenge.height - 20)
                    print("进入秘境", mjxyLocation)
                    cooldown(2)
                    return True


        return False


    def do(self):
        if self.run_mjxy() is False:
            return

        i = 0
        while self._flag:
            t = 2 if i == 0 else 30
            cooldown(t)
            i += 1
            if i % 10 == 0: # 每5分钟检测下
                # if self.run_mjxy() is False:
                #     return
                i = 10

            # 战斗标识
            battleLoc = Util.locateOnScreen('resources/small/enter_battle_flag.png')
            if battleLoc is not None:
                continue

            mjxyFail = Util.locateCenterOnScreen('resources/mjxy/mjxy_fail.png')
            if mjxyFail is not None:
                pyautogui.rightClick(mjxyFail.x, mjxyFail.y)
                self.use_item()
                print("失败了，结束秘境", mjxyFail)

                cooldown(1)
                mjxyLeave = Util.locateCenterOnScreen('resources/mjxy/mjxy_leave.png')
                pyautogui.leftClick(mjxyLeave.x, mjxyLeave.y)
                print("秘境通关，离开", mjxyLeave)
                return

            cooldown(2)
            self.use_item()

            cooldown(2)
            mjxyFight = Util.locateCenterOnScreen('resources/mjxy/mjxy_fight.png')
            if mjxyFight is not None:
                pyautogui.leftClick(mjxyFight.x, mjxyFight.y)
                print("秘境，进入战斗", mjxyFight)

            cooldown(2)
            mjxyLocation = Util.locateCenterOnScreen('resources/mjxy/mjxy_pos.png')
            print(f"===== mjxyLocation:{mjxyLocation}")
            if mjxyLocation is not None:
                pyautogui.leftClick(mjxyLocation.x, mjxyLocation.y)
                print("继续秘境", mjxyLocation)
            
            cooldown(2)
            mjxyFight = Util.locateCenterOnScreen('resources/mjxy/mjxy_fight.png')
            if mjxyFight is not None:
                pyautogui.leftClick(mjxyFight.x, mjxyFight.y)
                print("秘境，进入战斗", mjxyFight)

            cooldown(2)
            mjxyPass = Util.locateCenterOnScreen('resources/mjxy/mjxy_pass.png')
            if mjxyPass is not None:
                self.use_item()

                cooldown(2)
                mjxyLeave = Util.locateCenterOnScreen('resources/mjxy/mjxy_leave.png')
                pyautogui.leftClick(mjxyLeave.x, mjxyLeave.y)
                print("秘境通关，离开", mjxyLeave)
                return


if __name__ == '__main__':
    Mjxy().do()
