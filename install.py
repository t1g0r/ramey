from pymongo import MongoClient


client = MongoClient()
db = client.ramey

print "Ramey Instalation"
print "========================"

print "installing db data.."

print "- table users"
#create default users
db.users.insert([
	{
		"_id":"ramey",
		"userid":"ramey",
		"pwd":"0558d3dd05c436844318664582ec1d08",
		"fullname":"Ramey",
		"active":1
	},
	{
		"_id":"tigor",
		"userid":"tigor",
		"pwd":"0558d3dd05c436844318664582ec1d08",
		"fullname":"Tigor Mangatur Manurung",
		"active":1
	},
	])

print "- table users_account"
#user_account
db.users_account.insert([
	{
		"userid":"ramey",
		"account_alias":"username",
		"type":"telegram",
		"active":1
	}
	])

print "- command mapper"
#command mapper
db.commandmapper.insert([
	{
		"_id":"ceklamp",
		"commandkey":"ceklamp",
		"commandname":"Cek Lampu",
		"class_ref":"LampHandler.ceklamp",
		"gpios":"1"
	},
	{
    "_id" : "hidupkanlampu",
    "gpios" : "6,22",
    "commandkey" : "hidupkanlampu",
    "commandname" : "Hidupkan Lampu",
    "class_ref" : "SwitchHandler.switchon"
	},
	{
    "_id" : "matikanlampu",
    "gpios" : "6,22",
    "commandkey" : "matikanlampu",
    "commandname" : "Matikan Lampu",
    "class_ref" : "SwitchHandler.switchoff"
	},
	{
    "_id" : "bunyikanbuzzer",
    "gpios" : "5,25",
    "commandkey" : "bunyikanbuzzer",
    "commandname" : "Bunyikan Buzzer",
    "class_ref" : "SwitchHandler.echo"
	},
	{
		"_id":"fotodong",
		"commandkey":"fotodong",
		"commandname":"Ambil Foto",
		"class_ref":"CameraHandler.fotodong"
	},
	{
		"_id":"daftarid",
		"commandkey":"daftarid",
		"commandname":"Pendaftaran Kartu Akses",
		"class_ref":"CardHandler.daftarid"
	},
	{
		"_id":"lepasid",
		"commandkey":"lepasid",
		"commandname":"Pelepasan Kartu Akses",
		"class_ref":"CardHandler.lepasid"
	},
	{
    "_id" : "hidupkansensor",
    "commandkey" : "hidupkansensor",
    "commandname" : "Hidupkan Sensor",
    "gpios" : "20",
    "buzzer" : "25",
    "class_ref" : "SensorHandler.switchon"
	},
	{
    "_id" : "matikansensor",
    "commandkey" : "matikansensor",
    "commandname" : "Matikan Sensor",
    "gpios" : "20",
    "buzzer" : "25",
    "class_ref" : "SensorHandler.switchoff"
	},
	{
		"_id":"ceksemua",
		"commandkey":"ceksemua",
		"commandname":"Cek Alarm",
		"class_ref":"CheckHandler.ceksemua"
	}
	])

print "- table parameter"
#params 
db.params.insert([
	{
		"_id":"needauth",
		"value":1
	},
	{
    "_id" : "sensor_motion",
    "value" : "20",
    "buzzer" : "22,25",
    "active" : true
	},
	{
    "_id" : "alarm_message",
    "value" : "Ada gerakan terdeteksi!"
	}
	])

print "db data OK"

print "Done."
