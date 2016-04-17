import sys
import os
sys.path.append("backend/gateway/")
from telegw import ryTelegramGw
from pymongo import MongoClient

import json

with open("config.json") as jsonf:
	config = json.load(jsonf)

# config["ROOTPATH"] = "/Users/tigormanurung/Documents/WORKS/JLS/ramey/"
client = MongoClient()
db = client.ramey

bot = ryTelegramGw(config,db)
bot.connect()