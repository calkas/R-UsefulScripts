#!/usr/bin/python
import pyautogui
import time

#pyautogui.alert('Stay alive script. Sleep Time: ' + str(REFRESH_TIME))
REFRESH_TIME = pyautogui.prompt('Stay alive script. Set refresh time in [s]')
if not REFRESH_TIME:
	REFRESH_TIME = 60.0

print "Refresh Time: " + str(REFRESH_TIME) + " seconds"

while True:
    pyautogui.press('f15')
    timeStr = time.ctime()
    print("Log: [" + timeStr + "] Key Pressed - stay alive!")
    time.sleep(float(REFRESH_TIME))


