import sys,os
from pymongo import MongoClient
import importlib
import LampHandler
import CameraHandler
from pprint import pprint


class CommandHandler(object):
	"""docstring for CommandHandler"""
	def __init__(self, dbconn, command,callback,callback2):
		super(CommandHandler, self).__init__()
		self.dbconn = dbconn
		self.command = command
		self.params = {}
		self.params["callback"] = callback
		self.params["callback2"] = callback2
		self.params["command"] = self.command

		self.callback = callback
		self.callback2 = callback2

		# self.callbacks = [self.callback,self.callback2]
		
		
	def execute(self):
		commandstr = self.command["message"][1:]
		cCommand = self.dbconn.commandmapper.find({"commandkey":commandstr}).limit(1)

		#if commmand is not found, then send response
		if cCommand.count() > 0:
			cCommand = cCommand[0]
			# print cCommand.count()
			self.callback(self.command["account_id"],"hii %s, you just sent command name : '%s' and this is callback!" % (self.command["fullname"],cCommand["commandname"]))

			try:
				#execute command
				#get package
				module = eval(cCommand["class_ref"])

				#get class
				class_ = getattr(module, cCommand["class_ref"])

				#init
				instance = class_(self.dbconn,self.params)

				#exec
				instance.execute()
			except Exception, e:
				self.callback(self.command["account_id"],"Unhandled Command [%s]" % e)
		else:
			self.callback(self.command["account_id"],"Unknown Command.")