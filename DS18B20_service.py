from flask import Flask, jsonify

app = Flask(__name__)

from DS18B20_helper import ds18b20_helper

@app.route("/DS18B20/c")
def celcius():
    celcius,farenheit = ds18b20_helper.read_temp()
    rc = {"value": celcius}
    print("C:" + str(rc))
    return jsonify(rc)
    
@app.route("/DS18B20/f")
def farenheit():
    celcius,farenheit = ds18b20_helper.read_temp()
    rc = {"value": farenheit}
    print("C:" + str(rc))
    return jsonify(rc)
    
