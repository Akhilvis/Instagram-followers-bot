import pyautogui
from random import randint
from time import sleep

currentMouseX, currentMouseY = pyautogui.position()

print(currentMouseX, currentMouseY)


for _ in range(10):
	y_position_follow_button = 400
	for _ in range(6):

		pyautogui.moveTo(1200, y_position_follow_button)
		pyautogui.click()

		sleep(randint(1,5))


		pyautogui.moveTo(1130, 690) 
		pyautogui.click()

		y_position_follow_button += 80

		sleep(randint(1,7))

	pyautogui.scroll(-10000)
