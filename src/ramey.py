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
	cfg = json.load(jsonf)

client = MongoClient()
db = client.ramey


# # config = {}
# cfg["pin"] = Parameter.getValue(db,"sensor_motion")
# cfg["dbconn"] = db
# motion = MotionSensor(cfg)
# utils.newThread(motion.Execute)

cfg["name"] = "telegram"
bot = ryTelegramGw(config=cfg,dbconn=db,sensor=motion)
bot.connect()