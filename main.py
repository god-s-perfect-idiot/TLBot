import time
import os

while(True):
	try:
		os.system('talklifebot.py')
		print("?")
	except Exception as e:
		print(e)
	time.sleep(180)
