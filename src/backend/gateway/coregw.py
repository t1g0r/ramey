import sys,os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from command import Handler
from pymongo import MongoClient
import datetime
from pprint import pprint
from utils import Parameter


# sys.path.append(os.path.join(os.path.dirname(__file__), '..','..'))


class ryCoreGateway(object):
	"""docstring for ryCoreGateway"""
	def __init__(self,config,dbconn,sensor,user=None,pwd=None):
		self.dbconn = dbconn
		self.user = user
		self.pwd = pwd
		self.active = False
		self.sensor = sensor
		self.sensor.AddCallback(self.onMotion)

		self.config = config
		self.name = self.config["name"]

		

		
	def connect(self):
		pass

	def disconnect(self):
		self.active = False

	def sendMessage(self,to,message):
		pass

	def sendPhoto(self,to,filepath):
		pass

	def onMotion(self):
		# users = self.dbconn.users.find({"active":1},{"userid":1})
		# users_account = self.dbconn.users_account.find({"type":"%s"%self.name,"userid":{"$in":users["userid"]}})

		users = self.dbconn.users.find({"active":1},{"userid":1,"_id":0})
		for user in users:
			users_account = self.dbconn.users_account.find({"active":1,"type":"%s" % self.name,"userid":{"$in":[user["userid"]]}})
			for account in users_account:
				self.sendMessage(account["account_id"], Parameter.getValue(self.dbconn,"alarm_message"))

	def onMessage(self,params):
		# print "=================PARAMS================="
		# pprint(params)
		self.dbconn.inbox.insert(params)
		# self.dbconn.inbox.insert({"from":params["account_id"],"msg":params["message"],"type":self.__class__.__name__,"cdate":datetime.datetime.now()})

		if params["message"] == "":
			return

		if params["message"][0] == "/":
			# params = {}
			# params["fromWho"] = fromWho
			# params["message"] = message
			self.onCommand(params)

	def onCommand(self,params):
		print "command detected! : %s" % params["account_id"]

		#cek user terdaftar atau tidak
		# pprint(params)
		cursor = self.dbconn.users_account.find({
			"$or" : [
				{"account_id":"%s" % params["account_id"]},
				{"account_alias":"%s" % params["account_name"]} 
			],
			"active" : 1
			})
		if cursor.count() > 0:
			#cek jika account_id kosong, maka diisi
			if cursor[0].get("account_id","") == "":
				self.dbconn.users_account.update({"_id":cursor[0]["_id"]},
					{"$set":
						{"account_id":"%s" % params["account_id"]}

					})

			if "account_name" in params:
				if cursor[0].get("account_alias","") == "":
					self.dbconn.users_account.update({"_id":cursor[0]["_id"]},
						{"$set":
							{"account_alias":"%s" % params["account_name"]}

						})
				# self.dbconn.users_account.update({"_id":cursor[0]["_id"]},{"account_alias":params["account_name"]})
			#jika ditemukan usernya, cek dulu apakah itu user aktif atau tidak
			cUser = self.dbconn.users.find({"userid":cursor[0]["userid"],"active":1})
			if cUser.count() > 0:
				params["fullname"] = cUser[0]["fullname"]
				params["sendmessage"] = self.sendMessage
				params["sendphoto"] = self.sendPhoto
				params["AppConfig"] = self.config
				params["sensor"] = self.sensor
				cmHandler = Handler(self.dbconn,params)
				cmHandler.execute()
				# self.disconnect()
		else:
			print "command not found!"

	def onCallback(self):
		print "here is callback"
		
	def onError(self,Exception):
		pass
