import time

while(True):
	try:
		execfile('talklifebot.py')
	except:
		time.sleep(60)
	time.sleep(180)
