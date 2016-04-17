import sys
from pprint import pprint
import threading

class Parameter(object):

		@staticmethod
		def getValue(dbconn,key):
			cdata = dbconn.params.find({"_id":"%s"%key})
			if cdata.count() > 0:
				return cdata[0]["value"]
			else:
				return ""

		@staticmethod
		def getValuebyFieldname(dbconn,key,fieldname):
			cdata = dbconn.params.find_one({"_id":"%s"%key})
			return cdata.get(fieldname,"")
			# if cdata.count() > 0:
			# 	return cdata[fieldname]
			# else:
			# 	return ""

def newThread(f,args=()):
		t = threading.Thread(target=f,args=args)
		t.deamon = True
		t.start()
		return t