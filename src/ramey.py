import sys
import os
sys.path.append("backend/gateway/")
from telegw import ryTelegramGw
from pymongo import MongoClient

import json

with open("config.json") as jsonf:
	config = json.load(jsonf)

client = MongoClient()
db = client.ramey

bot = ryTelegramGw(config,db,"dua","tiga")
bot.connect()