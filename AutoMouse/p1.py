import pyautogui

print(pyautogui.position())
i = 0
while i < 2:
    pyautogui.moveRel(0, 50, 1)
    a = pyautogui.position()
    pyautogui.doubleClick()
    pyautogui.moveTo(901, 44, 0.1)
    pyautogui.click()
    pyautogui.moveTo(698, 87, 0.5)
    pyautogui.click()
    pyautogui.moveTo(73, 242,3)
    pyautogui.click()
    pyautogui.moveTo(a[0], a[1],1)
    i = i+1
#pyautogui.scroll(-800)