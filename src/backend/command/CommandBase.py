from pprint import pprint

class CommandBase(object):
	"""docstring for CommandBase"""
	def __init__(self, dbconn,args):
		super(CommandBase, self).__init__()
		print "command base"
		self.dbconn = dbconn
		self.params = args
		# pprint(self.params)

		self.messageStr = self.params["command"]["message"][1:]
		self.AppConfig = self.params["command"]["AppConfig"]
		self.sensor = self.params["command"]["sensor"]

		if " " in self.messageStr:
			#get param
			self.methodParam = self.messageStr[self.messageStr.find(" ")+1:]
			#get method
			#self.methodStr = self.methodStr[:self.methodStr.find(" ")]

		#get pins from table
		self.Pins = self.dbconn.commandmapper.find({"_id":self.params["id"]})[0]
		#string to array, delimiter ','
		self.Pins = self.Pins.get("gpios","").split(',')
		pprint(self.Pins)
		# pprint(self.Pins.get('gpios'))

	def execute(self):
		print "%s executed!" % self.__class__.__name__
		pass

	def onFailed(self):
		pass

	def SelfCheck(self):
		pass