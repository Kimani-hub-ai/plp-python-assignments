class Vehicle:
    def move(self):
        print("This vehicle moves...")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing through the water...")

# Polymorphic behavior in action
def start_journey(vehicle):
    vehicle.move()
