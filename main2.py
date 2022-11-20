import pygetwindow
import pyautogui
from PIL import Image
import platform

path = 'C:\\Users\\Johnny\\Documents\\1dev\\python\\pokemmo_project\\result.png'
titles = pygetwindow.getAllTitles()

if platform.system() == 'Windows':
	window = pygetwindow.getWindowsWithTitle('PokeMMO')[1]
	left, top = window.topleft
	right, bottom = window.bottomright
	pyautogui.screenshot(path)
	im = Image.open(path)
	# im = im.crop((left, top, right, bottom))
	im.save(path)
	im.show(path)
