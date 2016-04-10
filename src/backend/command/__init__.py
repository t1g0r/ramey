import sys,os
from pymongo import MongoClient
import LampHandler
		

class CommandHandler(object):
	"""docstring for CommandHandler"""
	def __init__(self, dbconn, command,callback):
		super(CommandHandler, self).__init__()
		self.dbconn = dbconn
		self.command = command
		callback()

	def execute(self):
		pass
