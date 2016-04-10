import sys,os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from command import CommandHandler
from pymongo import MongoClient


# sys.path.append(os.path.join(os.path.dirname(__file__), '..','..'))


class ryCoreGateway(object):
	"""docstring for ryCoreGateway"""
	def __init__(self,dbconn,user,pwd):
		self.dbconn = dbconn
		self.user = user
		self.pwd = pwd
		self.active = False

		with open("../../config.json") as jsonf:
			self.config = json.load(jsonf)


	def connect(self):
		pass

	def disconnect(self):
		pass

	def sendMessage(self,to,message):
		pass

	def onMessage(self,fromWho,message):
		self.dbconn.inbox.insert({"from":fromWho,"msg":message,"type":self.__class__.__name__})

		if message[0] == "/":
			params = {}
			params["fromWho"] = fromWho
			params["message"] = message
			self.onCommand(fromWho,params)

	def onCommand(self,fromWho,params):
		print "command detected! : %s" % params["fromWho"]
		cmHandler = CommandHandler(self.dbconn,params,self.onCallback)
		cmHandler.execute()

	def onCallback(self):
		print "here is callback"
		
	def onError(self,Exception):
		pass
