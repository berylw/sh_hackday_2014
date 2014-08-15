import time
import urllib
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
	if (GPIO.input(21) == 0):
                time.sleep(1)
		print ("Button 21 is pressed - yes")
                urllib.urlopen("http://127.0.0.1:8000/question/vote/1").getcode()
        if (GPIO.input(13) == 0):
                #time.sleep(1)
		print ("Button 13 is pressed - no")
	        urllib.urlopen("http://127.0.0.1:8000/question/vote/0").getcode()
        time.sleep(0.05)
GPIO.cleanup()
