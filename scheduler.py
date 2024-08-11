import schedule
import time
from device_control import SmartLight, SmartThermostat

def turn_on_light():
    light = SmartLight("192.168.1.100")
    light.turn_on()

def set_night_temperature():
    thermostat = SmartThermostat("192.168.1.101")
    thermostat.set_temperature(68)

schedule.every().day.at("18:00").do(turn_on_light)
schedule.every().day.at("22:00").do(set_night_temperature)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
