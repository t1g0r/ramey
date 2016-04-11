import sys,os
from pymongo import MongoClient
import importlib
import LampHandler
from pprint import pprint


class CommandHandler(object):
	"""docstring for CommandHandler"""
	def __init__(self, dbconn, command,callback):
		super(CommandHandler, self).__init__()
		self.dbconn = dbconn
		self.command = command
		self.callback = callback
		
		
	def execute(self):
		commandstr = self.command["message"][1:]
		cCommand = self.dbconn.commandmapper.find({"commandkey":commandstr}).limit(1)

		#if commmand is not found, then send response
		if cCommand.count() > 0:
			cCommand = cCommand[0]
			# print cCommand.count()
			self.callback(self.command["fromWho"],"hii %s, you just sent command name : '%s' and this is callback!" % (self.command["fullname"],cCommand["commandname"]))

			try:
				#execute command
				#get package
				module = eval(cCommand["class_ref"])

				#get class
				class_ = getattr(module, cCommand["class_ref"])

				#init
				instance = class_(self.dbconn,None)

				#exec
				instance.execute()
			except Exception, e:
				self.callback(self.command["fromWho"],"Unhandled Command [%s]" % e)
		else:
			self.callback(self.command["fromWho"],"Unknown Command.")