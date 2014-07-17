import threading
import time
import sys

DIR = "/sys/bus/w1/devices/"
FILE = "/w1_slave"

class Temperature():
	def __init__(self, id):
		self.id = id
		self.file = DIR+id+FILE

	def getTempC(self):
		termfile = open(self.file, "r")
		parselines = termfile.readlines()
		if parselines[0].strip()[-3:] == "YES":
			equals_pos = parselines[1].find("t=")
			if equals_pos != -1:
				gradestring = parselines[1][equals_pos+2:]
				return (float(gradestring)/1000)
			else:
				print "Not temperature"
				sys.stdout.flush()
		else:
			print "Sensor state=OFF"
			sys.stdout.flush()
		termfile.close()
		return -1