import time
from updateInfo import UpdateInfo
from updateRedis import UpdateRedis
from maintelnet import mainServer
import socket
from Temp import Temperature
from updateTemp import UpdateTemp
from XMLReader import XMLReader
from SetValue import SetValue

config = XMLReader('../config/config.xml')
ms = mainServer()
ms.start()
tempcontrol = Temperature(config.getSensorID())
setv = SetValue()
configurl = config.getConfigURL()
tempurl = config.getUpgradeTempURL()
while True:
	update = UpdateInfo(config.getUsername(),config.getPassword(), configurl)
	info = update.getDBInfo()
	redis = UpdateRedis(info, 'lastcommit')
	redis.update()
	grade=tempcontrol.getTempC();
	updtemp = UpdateTemp(grade, config.getUsername(), config.getPassword(), tempurl)
	updtemp.update()
	setv.check(grade,info)
	time.sleep(5)