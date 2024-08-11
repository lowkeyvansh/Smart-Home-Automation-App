from flask import Flask, request, jsonify
from device_control import SmartLight, SmartThermostat

app = Flask(__name__)

light = SmartLight("192.168.1.100")
thermostat = SmartThermostat("192.168.1.101")

@app.route('/light/on', methods=['POST'])
def light_on():
    response = light.turn_on()
    return jsonify(response)

@app.route('/light/off', methods=['POST'])
def light_off():
    response = light.turn_off()
    return jsonify(response)

@app.route('/thermostat/set', methods=['POST'])
def set_temperature():
    temperature = request.json.get("temperature")
    response = thermostat.set_temperature(temperature)
    return jsonify(response)

@app.route('/thermostat/get', methods=['GET'])
def get_temperature():
    response = thermostat.get_temperature()
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
