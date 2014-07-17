import urllib
import urllib2
import redis
import sys

class SendTemp:

	def __init__(self,username, password, temp, url):
		self.username = username
		self.password = password
		self.temp = temp
		self.url = url

	def send(self):
		url = self.url
		values = {'username' : self.username, 'password' : self.password ,'currenttemp' : self.temp }
		try:
			data = urllib.urlencode(values)
			req = urllib2.Request(url, data)
			response = urllib2.urlopen(req, timeout = 2)
			the_page = response.read()
			#print the_page
			sys.stdout.flush()
		except:
			print "Updating Temperature Locked..."
			sys.stdout.flush()