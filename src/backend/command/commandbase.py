class CommandBase(object):
	"""docstring for CommandBase"""
	def __init__(self, dbconn,args):
		super(CommandBase, self).__init__()
		self.dbconn = dbconn
		self.args = args

	def execute(self):
		print "%s executed!" % self.__class__.__name__
		pass

	def onFailed(self):
		pass