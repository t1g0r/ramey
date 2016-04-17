import sys
import os
sys.path.append("backend/gateway/")
sys.path.append("backend/")
sys.path.append("utils/")
from utils import Parameter
import utils
from telegw import ryTelegramGw
from pymongo import MongoClient
from sensor import MotionSensor

import json

with open("config.json") as jsonf:
	config = json.load(jsonf)

client = MongoClient()
db = client.ramey


print Parameter.getValue(db,"sensor_motion")
config = {}
config["pin"] = Parameter.getValue(db,"sensor_motion")
config["dbconn"] = db
motion = MotionSensor(config)
utils.newThread(motion.Execute)

config["name"] = "telegram"
bot = ryTelegramGw(config,db,sensor=motion)
bot.connect()