import sys,os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from command import Handler
from pymongo import MongoClient
import datetime
from pprint import pprint


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
		self.active = False

	def sendMessage(self,to,message):
		pass

	def onMessage(self,fromWho,message):
		self.dbconn.inbox.insert({"from":fromWho,"msg":message,"type":self.__class__.__name__,"cdate":datetime.datetime.now()})

		if message[0] == "/":
			params = {}
			params["fromWho"] = fromWho
			params["message"] = message
			self.onCommand(fromWho,params)

	def onCommand(self,fromWho,params):
		print "command detected! : %s" % params["fromWho"]

		#cek user terdaftar atau tidak
		cursor = self.dbconn.users_account.find({"account_id":"%s"%fromWho,"active":1})
		if cursor.count() > 0:
			#jika ditemukan usernya, cek dulu apakah itu user aktif atau tidak
			cUser = self.dbconn.users.find({"userid":cursor[0]["userid"],"active":1})
			if cUser.count() > 0:
				params["fullname"] = cUser[0]["fullname"]
				cmHandler = Handler(self.dbconn,params,self.sendMessage)
				cmHandler.execute()
				# self.disconnect()

	def onCallback(self):
		print "here is callback"
		
	def onError(self,Exception):
		pass
