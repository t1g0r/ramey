class CommandBase(object):
	"""docstring for CommandBase"""
	def __init__(self, args):
		super(CommandBase, self).__init__()
		self.args = args

	def execute(self):
		pass

	def onFailed(self):
		pass