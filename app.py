from ctypes import pythonapi
import pyautogui
import time

# positio = pyautogui.position()
# print(positio)
# pyautogui.KEYBOARD_KEYS

# pyautogui.alert("Iniciando automação")
pyautogui.PAUSE = 0.5
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("https://admin.google.com/")
pyautogui.press("enter")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("tab")
time.sleep(1)
pyautogui.write("Relatório")
time.sleep(1)
pyautogui.moveTo(428,262)
pyautogui.press("enter")
time.sleep(2)
pyautogui.moveTo(1221,275)
pyautogui.click(button='left')
pyautogui.press("enter")



