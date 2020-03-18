from flask import Flask, request, jsonify
import requests
import json
import os.path

def getExistance(fullFileName):
	if(os.path.isfile(fullFileName)):
		with open(fullFileName) as json_data:
			jsonFile = json.load(json_data)
		os.remove(fullFileName)
		return jsonFile
	else:
		return "0"  #  OK

app = Flask(__name__)

myHost = "192.168.0.102"
myPort = 8090

@app.route("/")
def hello():
	print("val")
	return "Hello World!"

@app.route('/postOrder/<id>', methods = ['POST'])
def postJsonOrder(id):
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	path = BASE_DIR + "/Orders/"
	filename = "Order" + str(id)
	content = request.get_json()
	jjson = { "MachineID": int(content['MachineID']),
			"type": str(content['type']),
			"strenght": int(content['strenght']),
			"volume": int(content['volume']),
			"milk": bool(content['milk']),
			"shugar": int(content['shugar'])
		}

	js = json.dumps(jjson, sort_keys=True, indent=4, separators=(',', ': '))
	with open (path + filename + '.json', 'w+') as f:
		f.write(js)

	return "#" # OK 

@app.route('/postToken/<id>', methods = ['POST'])
def postJsonToken(id):
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	path = BASE_DIR + "/Tokens/"
	filename = "Token" + str(id)
	content = request.get_json()
	jjson = {'token':content['token']}
	js = json.dumps(jjson, sort_keys=True, indent=4, separators=(',', ': '))
	with open (path + filename + '.json', 'w+') as f:
		f.write(js)

	return "#"   # OK

@app.route('/postTokenStatus/<id>', methods = ['POST'])
def postTokenStatus(id):
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	path = BASE_DIR + "/TokenStatuses/"
	filename = "TokenStatus" + str(id)

	content = request.get_json()
	jjson = {'status':content['status']}
	js = json.dumps(jjson, sort_keys=True, indent=4, separators=(',', ': '))
	with open (path + filename + '.json', 'w+') as f:
		f.write(js)
	
	return "#"   # OK

@app.route('/postOrderStatus/<id>', methods = ['POST'])
def postOrderStatus(id):
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	path = BASE_DIR + "/OrderStatuses/"
	filename = "OrderStatus" + str(id)

	content = request.get_json()
	jjson = {'status': content['status']}
	js = json.dumps(jjson, sort_keys=True, indent=4, separators=(',', ': '))
	with open (path + filename + '.json', 'w+') as f:
		f.write(js)
	
	return "#"   # OK

@app.route('/getToken/<id>') #  OK
def getJsonToken(id):
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	path = BASE_DIR + "/Tokens/"
	filename = 'Token' + str(id) + '.json'
	return jsonify(getExistance(path + filename))

@app.route('/getOrder/<id>') #  OK
def getJsonOrder(id):
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	path = BASE_DIR + "/Orders/"
	filename = 'Order' + str(id) + '.json'
	return jsonify(getExistance(path + filename))

@app.route('/getTokenStatus/<id>') #  OK
def getTokenStatus(id):
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	path = BASE_DIR + "/TokenStatuses/"
	filename = 'TokenStatus' + str(id) + '.json'
	jsonFile = getExistance(path + filename)
	if (jsonFile == "0"):
		return "0"
	else:
		return jsonFile['status']

@app.route('/getOrderStatus/<id>') #  OK
def getOrderStatus(id):
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	path = BASE_DIR + "/OrderStatuses/"
	filename = 'OrderStatus' + str(id) + '.json'
	jsonFile = getExistance(path + filename)
	if (jsonFile == "0"):
		return "0"
	else:
		return jsonFile['status']

if __name__ == '__main__':
	app.run(host=myHost, port=myPort)
