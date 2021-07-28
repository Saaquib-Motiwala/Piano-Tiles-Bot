import pyautogui
import win32api, win32con
import time
import keyboard

# x = 729, y = 600
# x = 882, y = 600
# x = 1025, y = 600
# x = 1159, y = 600


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


time.sleep(1)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(729, 600)[0] == 0:
        click(729, 600)
    if pyautogui.pixel(882, 600)[0] == 0:
        click(882, 600)
    if pyautogui.pixel(1025, 600)[0] == 0:
        click(729, 600)
    if pyautogui.pixel(1159, 600)[0] == 0:
        click(729, 600)
