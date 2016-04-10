from pymongo import MongoClient


client = MongoClient()
db = client.ramey

# datas = db.commandmapper.find({"commandkey":{"$exists":True}})
# data = db.commandmapper.find({"commandkey":"ceklamp"}).limit(1)
data = db.commandmapper.find().limit(1)
print data.count()
# for data in datas:
# 	print data