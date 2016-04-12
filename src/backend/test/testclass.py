import sys


class testcoba(object):
	"""docstring for testcoba"""
	def __init__(self, name,age,sex=None):
		super(testcoba, self).__init__()
		self.name = name
		self.age = age
		self.sex = sex

coba = testcoba(name="tigor",age="satu")
