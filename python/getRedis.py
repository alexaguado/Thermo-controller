import redis
import json
import sys

class GetRedis:

	def __init__(self):
		print "reading info..."
		sys.stdout.flush()

	def get(self, op):
		pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
		r = redis.Redis(connection_pool=pool)
		if op==1:
			lastcommit = r.get('lastcommit')
			decoded = json.loads(lastcommit)
			return "State: "+decoded['state']+" Temperature: "+decoded['temperature']
		if op==2:
			temp = r.get('currentTemp')
			return "Current Temperature: "+temp
