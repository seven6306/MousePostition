from time import sleep
from keyboard import add_hotkey, remove_hotkey
from win32api import GetCursorPos, mouse_event

def getPoints():
	global counter
	x, y = GetCursorPos()
	counter = counter + 1
	print('Point {0}:\tx={1}'.format(str(counter), str(x)), 'y=' + str(y))
	
try:
	counter = 0
	add_hotkey('F10', lambda: getPoints())
	print('Press "Ctrl + C"  to exit')
	while(1):
		sleep(1)
except KeyboardInterrupt:
	remove_hotkey('F10')
