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

	def onMessage(self,userId,msgId,*args):
		#call inheritance
		super(ryTelegramGw,self).onMessage(*args)

		# self.dbconn.inbox.insert({"from":args[0],"msg":args[1],"msg_id":msgId,"type":self.__class__.__name__})
		print "message id : %s, from : %s, text : %s" % (msgId,args[0],args[1])

	def onRecMsg(self,msg):
		#pprint(msg)
		self.onMessage(msg["chat"].get("username",""),msg["message_id"],msg["from"]["id"],msg["text"])

	def sendMessage(self,to,message):
		self.bot.sendMessage(to,message)


client = MongoClient()
db = client.ramey

bot = ryTelegramGw(db,"dua","tiga")
bot.connect()
		