import RPi.GPIO as GPIO
import time
import json
import sys



class SetValue:

	def __init__(self):
		self.ison=False

	def check(self, temp, value):
		try:
			GPIO.setmode(GPIO.BOARD)
			# Set up header pin 11 (GPIO17) as an input
			# print "Setup Pin 11"
			GPIO.setup(11, GPIO.OUT)
			decoded = json.loads(value)
			state = decoded['state']
			temp2 = float(decoded['temperature'])
			sys.stdout.flush()
			if self.ison == False and "on" in state and temp2 > temp:
				GPIO.output(11,True)
				self.ison = True
				print "Turn ON"
				sys.stdout.flush()
			if self.ison == True and "off" in state:
				GPIO.output(11, False)
				self.ison = False
				print "Turn OFF"
				sys.stdout.flush()
			if self.ison == True and temp2 < temp:
				GPIO.output(11, False)
				self.ison = False
				print "Turn OFF"
				sys.stdout.flush()
		except:
			print "Avoiding decoding errors..."
			sys.stdout.flush()