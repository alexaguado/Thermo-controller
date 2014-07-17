import urllib
import urllib2
import redis
import sys

class UpdateInfo:

	def __init__(self,username, password, url):
		self.username = username
		self.password = password
		self.url = url

	def getDBInfo(self):
		url = self.url
		values = {'username' : self.username, 'password' : self.password }
		try:
			data = urllib.urlencode(values)
			req = urllib2.Request(url, data)
			response = urllib2.urlopen(req, timeout = 2)
			the_page = response.read()
			return the_page
		except:
			print "Downloading Commit Locked..."
			sys.stdout.flush()
