import sys
from CommandBase import CommandBase
from pprint import pprint


class CameraHandler(CommandBase):
	"""docstring for CameraHandler"""
	def __init__(self, *args):
		super(CameraHandler, self).__init__(*args)
		self.args = args

	def execute(self):
		super(CameraHandler,self).execute()
		#sample pic
		strPath = 'res/chart.png';
		print "Sending Photo.."
		self.args[1]["callback2"](self.args[1]["command"]["account_id"],strPath)
