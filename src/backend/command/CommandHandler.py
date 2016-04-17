import sys,os
from pymongo import MongoClient
import importlib
import SwitchHandler
import CameraHandler
from pprint import pprint


class CommandHandler(object):
	"""docstring for CommandHandler"""
	def __init__(self, dbconn, command):
		super(CommandHandler, self).__init__()
		self.dbconn = dbconn
		self.command = command
		self.params = {}
		self.params["callback"] = command["sendmessage"] #callback
		self.params["callback2"] = command["sendphoto"] #callback2
		self.params["command"] = self.command
		self.AppConfig = self.command["AppConfig"]
		pprint(self.AppConfig)

		# self.callback = callback
		# self.callback2 = callback2

		# self.callbacks = [self.callback,self.callback2]
		
		
	def execute(self):
		commandstr = self.command["message"][1:]
		if " " in commandstr:
			commandstr = commandstr[:commandstr.find(" ")]
		# print "Command : '%s'" % commandstr
		print "get from db"
		cCommand = self.dbconn.commandmapper.find({"commandkey":commandstr}).limit(1)
		print "get db selesai"
		#if commmand is not found, then send response
		if cCommand.count() > 0:
			cCommand = cCommand[0]
			self.params["callback"](self.command["account_id"],"hii %s, you just sent command name : '%s' and this is callback!" % (self.command["fullname"],cCommand["commandname"]))

			try:
				#execute command
				#get package
				self.modules = cCommand["class_ref"].split(".")

				#fill params
				self.params["class"] = self.modules[0]
				self.params["method"] = self.modules[1]
				self.params["id"] = cCommand["_id"]

				# module = sys.modules[self.modules[0]]
				# pprint(module)
				module = eval(self.modules[0])
				#get class
				class_ = getattr(module, self.modules[0])
				#init
				instance = class_(self.dbconn,self.params)
				#exec
				instance.execute()
			except Exception, e:
				self.callback(self.command["account_id"],"Unhandled Command [%s]" % e)
				raise e
		else:
			self.callback(self.command["account_id"],"Unknown Command.")