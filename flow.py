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