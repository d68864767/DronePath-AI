```python
from coordinates import Coordinates
from obstacle import Obstacle, NoFlyZone
from search import Search
from weather import Weather, WeatherData
from drone import Drone
from task import Task, TaskType
from path_calculator import PathCalculator

def main():
    # Initialize the Search object with the OpenWeatherMap API key
    search = Search("your_openweathermap_api_key")

    # Initialize the Weather object
    weather = Weather(search)

    # Initialize the Drone object at the starting coordinates
    drone = Drone(Coordinates(0, 0), weather)

    # Initialize the Task object with the task type, destination, obstacles, and no-fly zones
    task = Task(TaskType.DELIVERY, Coordinates(10, 10), [Obstacle(Coordinates(5, 5))], [NoFlyZone(Coordinates(7, 7))])

    # Initialize the PathCalculator object
    path_calculator = PathCalculator(drone, task)

    # Calculate the path
    path = path_calculator.calculate_path()

    # Move the drone along the path
    for coordinates in path:
        drone.move_to(coordinates)

    # Print the final drone status
    print(drone)

if __name__ == "__main__":
    main()
```
