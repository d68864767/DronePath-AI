```python
class Weather:
    def __init__(self, search):
        self.search = search

    def get_current_weather(self, coordinates):
        weather_data = self.search.get_weather(coordinates)
        if weather_data is not None:
            return WeatherData(weather_data)
        else:
            return None


class WeatherData:
    def __init__(self, data):
        self.temperature = data["temperature"]
        self.humidity = data["humidity"]
        self.pressure = data["pressure"]
        self.wind_speed = data["wind_speed"]
        self.wind_direction = data["wind_direction"]

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

    def get_wind_speed(self):
        return self.wind_speed

    def get_wind_direction(self):
        return self.wind_direction
```
