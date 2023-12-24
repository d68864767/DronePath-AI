```python
from coordinates import Coordinates

class Obstacle:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def get_coordinates(self):
        return self.coordinates

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def __str__(self):
        return f"Obstacle at {self.coordinates}"

class NoFlyZone:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def get_coordinates(self):
        return self.coordinates

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def __str__(self):
        return f"No-Fly Zone at {self.coordinates}"
```
