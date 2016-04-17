from pymongo import MongoClient
from pprint import pprint


client = MongoClient()
db = client.ramey

# datas = db.commandmapper.find({"commandkey":{"$exists":True}})
# data = db.commandmapper.find({"commandkey":"ceklamp"}).limit(1)
# # data = db.commandmapper.find().limit(1)
# data = db.params.find_one({"_id":"sensor_motion"})
# print data
# print data.count()
# for data in datas:
# 	print data

users = db.users.find({"active":1},{"userid":1,"_id":0})
for user in users:
	print user
	users_account = db.users_account.find({"type":"telegram","userid":{"$in":[user["userid"]]}})
	pprint(users_account)

# users_account = db.users_account.find({"type":"telegram","userid":{"$in":[users]}})
# pprint(users_account.count())

# pprint(users)