```python
from coordinates import Coordinates
from weather import Weather

class Drone:
    def __init__(self, coordinates, weather):
        self.coordinates = coordinates
        self.weather = weather

    def get_coordinates(self):
        return self.coordinates

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def get_weather(self):
        return self.weather.get_current_weather(self.coordinates)

    def move_to(self, new_coordinates):
        # This is a placeholder function. In a real-world application, this function would control the drone's motors to move it to the new coordinates.
        # For the purpose of this project, we will simply update the drone's current coordinates.
        self.coordinates = new_coordinates

    def __str__(self):
        return f"Drone at {self.coordinates}, Weather: {self.get_weather()}"
```
