import pyautogui, time

for i in range(15):
    pyautogui.moveTo(100,100, 1)
    time.sleep(120)
    pyautogui.moveTo(200,100, 1)
    time.sleep(120)
    pyautogui.moveTo(200,200, 1)
    time.sleep(120)
    pyautogui.moveTo(100,200, 1)
    time.sleep(120)
