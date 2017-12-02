import requests 
import json
# import sendserial
import serial
import time
ser = serial.Serial('/dev/ttyACM0', 38400, timeout=1)
def senddata(litre):
    # ser.flush()
    # print str(litre)
    ser.write(str(litre)+'\n')   # read a '\n' terminated line
    # da = ser.readline()
    # print da

# senddata("123")

getdata = {
    "type": "select",
    "args": {
        "table": "DeviceAPI",
        "columns": [
            "*"
        ],
        "where": {
            "flag": {
                "$eq": False
            }
        }
    }
}

setdata = {
    "type": "update",
    "args": {
        "table": "DeviceAPI",
        "where": {
            "id": {
                "$eq": ""
            }
        },
        "$set": {
            "flag": True
        }
    }
}

authheaders = {
    "Content-Type": "application/json",
    "Authorization": "Bearer cfe1de63b4bc268f3bcab0e4016f1035470766b293f95177"
}
url = "https://data.diatonic70.hasura-app.io/v1/query"
# while True:
def startmotor(litre):
    litre = litre / 100
    senddata(litre)
    # senddata('13')
def setflag(id):
    setdata["args"]["where"]["id"]["$eq"] = id
    data = requests.request("POST",url, data=json.dumps(setdata), headers=authheaders)

while True:
    data = requests.request("POST",url, data=json.dumps(getdata), headers=authheaders)
    print data.json()
    if len(data.json()) > 0:
        parseddata = data.json()[0]
        if "liter" in parseddata:
            print parseddata
            setflag(parseddata["id"])
            startmotor(parseddata["liter"])
            time.sleep( +10)
    time.sleep(10)
    parseddata = {}

    # setflag(parseddata["id"])

# setdata["args"]["where"]["id"]["$eq"] = "3"
# data = requests.request("POST",url, data=json.dumps(setdata), headers=authheaders)
# print data.json()
