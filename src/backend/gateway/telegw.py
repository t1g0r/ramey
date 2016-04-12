import sys
import os
import time
from pymongo import MongoClient
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'libs'))
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
		self.bot = telepot.Bot(self.config["telegram_config"]["token"])

		self.bot.notifyOnMessage(self.onRecMsg)

		self.active = True

		try:
			while self.active:
				time.sleep(2.5) #2.5 seconds
			print "telegram bot is ended."
		except KeyboardInterrupt, e:
			raise e
		# response = bot.getUpdates()
		# pprint(response)

	def onMessage(self,*args):
		#call inheritance
		super(ryTelegramGw,self).onMessage(*args)

		param = args[0]
		# self.dbconn.inbox.insert({"from":args[0],"msg":args[1],"msg_id":msgId,"type":self.__class__.__name__})
		print "message id : %s, from : %s, text : %s" % (param["message_id"],param["account_id"],param["message"])

	def onRecMsg(self,msg):
		# pprint(msg)
		params = {}
		params["account_id"] = msg["from"]["id"]
		if "text" in msg:
			params["message"] = msg["text"]
		else:
			params["message"] = ""
		params["firstname"] = msg["chat"]["first_name"]
		params["lastname"] = msg["chat"]["last_name"]
		params["account_name"] = msg["chat"].get("username","")
		params["message_id"] = msg["message_id"]

		self.onMessage(params)

	def sendMessage(self,to,message):
		self.bot.sendMessage(to,message)

	def sendPhoto(self,to,filepath):
		super(ryTelegramGw,self).sendPhoto(to,filepath)
		f = open(filepath,"rb")
		self.bot.sendPhoto(to,f)
		pass


client = MongoClient()
db = client.ramey

bot = ryTelegramGw(db,"dua","tiga")
bot.connect()
		