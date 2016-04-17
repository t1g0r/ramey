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
		"_id":"hidupkanlampu",
		"commandkey":"hidupkanlampu",
		"commandname":"Hidupkan Lampu",
		"class_ref":"LampHandler.hidupkanlampu",
		"gpios":"1"
	},
	{
		"_id":"matikanlampu",
		"commandkey":"matikanlampu",
		"commandname":"Matikan Lampu",
		"class_ref":"LampHandler.matikanlampu",
		"gpios":"1"
	},
	{
		"_id":"bunyikanbuzzer",
		"commandkey":"bunyikanbuzzer",
		"commandname":"Bunyikan Buzzer",
		"class_ref":"BuzzerHandler.bunyikanbuzzer",
		"gpios":"3"
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
		"_id":"hidupkansensor",
		"commandkey":"hidupkansensor",
		"commandname":"Hidupkan Sensor",
		"class_ref":"MotionHandler.hidupkansensor"
	},
	{
		"_id":"matikansensor",
		"commandkey":"matikansensor",
		"commandname":"Matikan Sensor",
		"class_ref":"MotionHandler.matikansensor"
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
	}
	])

print "db data OK"

print "Done."
