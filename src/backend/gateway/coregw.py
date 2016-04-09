class ryCoreGateway(object):
	"""docstring for ryCoreGateway"""
	def __init__(self,dbconn,user,pwd):
		super(ryCoreGateway, self).__init__()
		self.dbconn = dbconn
		self.user = user
		self.pwd = pwd
		self.active = False

	def connect(self):
		pass

	def disconnect(self):
		pass

	def sendMessage(self,to,message):
		pass

	def onMessage(self,fromwho,message):
		pass
		
	def onError(self,Exception):
		pass