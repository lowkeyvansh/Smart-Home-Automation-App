import requests

class SmartLight:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def turn_on(self):
        response = requests.post(f"http://{self.ip_address}/turn_on")
        return response.json()

    def turn_off(self):
        response = requests.post(f"http://{self.ip_address}/turn_off")
        return response.json()

    def set_brightness(self, level):
        response = requests.post(f"http://{self.ip_address}/set_brightness", json={"level": level})
        return response.json()

class SmartThermostat:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def set_temperature(self, temperature):
        response = requests.post(f"http://{self.ip_address}/set_temperature", json={"temperature": temperature})
        return response.json()

    def get_temperature(self):
        response = requests.get(f"http://{self.ip_address}/get_temperature")
        return response.json()

# Example usage:
if __name__ == "__main__":
    light = SmartLight("192.168.1.100")
    thermostat = SmartThermostat("192.168.1.101")

    light.turn_on()
    thermostat.set_temperature(72)
