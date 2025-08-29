class Transportation:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def move(self):
        pass  # To be implemented by subclasses
    
    def get_info(self):
        return f"{self.name} with max speed of {self.speed}"

class Car(Transportation):
    def move(self):
        return f"{self.name} is driving on the road at {self.speed} mph! 🚗"

class Airplane(Transportation):
    def move(self):
        return f"{self.name} is flying through the air at {self.speed} mph! ✈️"

class Bicycle(Transportation):
    def move(self):
        return f"{self.name} is pedaling on the path at {self.speed} mph! 🚴"

class Boat(Transportation):
    def move(self):
        return f"{self.name} is sailing on water at {self.speed} knots! ⛵"

class Hoverboard(Transportation):
    def move(self):
        return f"{self.name} is hovering above ground at {self.speed} mph! 🛹"

# Function demonstrating polymorphism
def travel_show(vehicles):
    print("\n=== TRAVEL SHOWCASE ===")
    for vehicle in vehicles:
        print(vehicle.move())
        print(f"  - {vehicle.get_info()}")
        print("-" * 50)

# usage
if __name__ == "__main__":
    # Create different transportation vehicles
    vehicles = [
        Car("Tesla Model 3", 120),
        Airplane("Boeing 737", 500),
        Bicycle("Mountain Bike", 15),
        Boat("Speed Boat", 45),
        Hoverboard("Future Board", 10)
    ]
    
    # Demonstrate polymorphism
    travel_show(vehicles)
   