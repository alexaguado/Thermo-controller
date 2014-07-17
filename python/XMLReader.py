from xml.etree import ElementTree

class XMLReader:

	def __init__(self, filename):
		self.document = ElementTree.parse( filename )

	def getUsername(self):
		tag = self.document.find( 'login')
		username = tag.attrib['username']
		return username

	def getPassword(self):
		tag = self.document.find( 'login')
		password = tag.attrib['password']
		return password

	def getSensorID(self):
		tag = self.document.find('sensor')
		sensorid = tag.attrib['id']
		return sensorid

	def getTelnetIP(self):
		tag = self.document.find( 'telnet')
		ip = tag.attrib['ip']
		return ip

	def getTelnetPort(self):
		tag = self.document.find( 'telnet')
		port = tag.attrib['port']
		return port

	def getUpgradeTempURL(self):
		tag = self.document.find('webconfig')
		return tag.attrib['url']+tag.attrib['upgradetemp']

	def getConfigURL(self):
		tag = self.document.find('webconfig')
		return tag.attrib['url']+tag.attrib['getconfig']