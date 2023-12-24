```python
from enum import Enum
from coordinates import Coordinates
from obstacle import Obstacle, NoFlyZone
from drone import Drone

class TaskType(Enum):
    SURVEILLANCE = 1
    DELIVERY = 2

class Task:
    def __init__(self, task_type, destination, obstacles, no_fly_zones):
        self.task_type = task_type
        self.destination = destination
        self.obstacles = obstacles
        self.no_fly_zones = no_fly_zones

    def get_task_type(self):
        return self.task_type

    def get_destination(self):
        return self.destination

    def get_obstacles(self):
        return self.obstacles

    def get_no_fly_zones(self):
        return self.no_fly_zones

    def set_task_type(self, task_type):
        self.task_type = task_type

    def set_destination(self, destination):
        self.destination = destination

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles

    def set_no_fly_zones(self, no_fly_zones):
        self.no_fly_zones = no_fly_zones

    def __str__(self):
        return f"Task: {self.task_type.name}, Destination: {self.destination}, Obstacles: {len(self.obstacles)}, No-Fly Zones: {len(self.no_fly_zones)}"
```
