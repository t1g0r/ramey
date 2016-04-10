import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'libs'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..','..'))
from pprint import pprint
#sys.path.append("../libs/")
# print sys.path
import telepot
from coregw import ryCoreGateway

class ryTelegramGw(ryCoreGateway):
	"""docstring for ryTelegramGw"""
	def __init__(self, *args):
		super(ryTelegramGw, self).__init__(*args)

	def connect(self):
		print "token telegram is %s" % self.config["telegram_config"]["token"]
		bot = telepot.Bot(self.config["telegram_config"]["token"])
		# response = bot.getUpdates()
		# pprint(response)


# bot = ryTelegramGw("satu","dua","tiga")
#bot.connect()
		