import redis
import sys

class UpdateRedis:

	def __init__(self,message, key):
		self.message = message
		self.key = key

	def update(self):
		pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
		r = redis.Redis(connection_pool=pool)
		lastcommit = r.get(self.key)
		#print lastcommit
		#print self.message
		sys.stdout.flush()
		if lastcommit != self.message:
			#print 'updating...'
			sys.stdout.flush()
			r.set(self.key, self.message)