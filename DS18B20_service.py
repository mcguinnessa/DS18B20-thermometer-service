from flask import Flask, jsonify

app = Flask(__name__)

from DS18B20_helper import ds18b20_helper

C_INDEX = 0
F_INDEX = 1

######################################################################
#
# Get temperature with given index, format for errors
#
######################################################################
def get_temperature(idx):

    try:
       rc =  {"value": ds18b20_helper.read_temp()[idx]}
    except ds18b20_helper.DeviceException as e:
       print("Exception:" + str(e))
       rc = {"error:": "Device Not Found"}
    except ds18b20_helper.DeviceFormatException as e:
       print("Exception:" + str(e))
       rc = {"error:": "Unexpected Format from device" }

    print("T:" + str(rc))
    return jsonify(rc)


######################################################################
#
# Get temperature in Celcius
#
######################################################################
@app.route("/DS18B20/c")
def celcius():
   return get_temperature(C_INDEX)
    
######################################################################
#
# Get temperature in Farenheit
#
######################################################################
@app.route("/DS18B20/f")
def farenheit():
   return get_temperature(F_INDEX)
#    celcius,farenheit = ds18b20_helper.read_temp()
#    rc = {"value": farenheit}
#    print("C:" + str(rc))
#    return jsonify(rc)
    
