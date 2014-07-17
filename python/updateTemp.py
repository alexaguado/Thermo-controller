from updateRedis import UpdateRedis
from sendTemp import SendTemp


class UpdateTemp:

	def __init__(self,message,username, password, url):
		self.message = message
		self.username = username
		self.password = password
		self.url = url

	def update(self):
		redis = UpdateRedis(self.message, "currentTemp")
		redis.update()
		temp = SendTemp(self.username, self.password, self.message, self.url)
		temp.send()