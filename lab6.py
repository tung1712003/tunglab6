class Car:
    def __init__(self, tank_capacity, fuel_consumption, average_speed):
        self.tank_capacity = tank_capacity
        self.fuel_consumption = fuel_consumption
        self.average_speed = average_speed

    def calculate_distance(self):
        distance = self.tank_capacity / self.fuel_consumption
        return distance
    def __add__(self, other):
        return Car(self.average_speed + other.average_speed)

class Truck(Car):
    def __init__(self, tank_capacity, fuel_consumption, average_speed, cargo_weight):
        super().__init__(tank_capacity, fuel_consumption, average_speed)
        self.cargo_weight = cargo_weight

    def calculate_ratio(self):
        ratio = self.cargo_weight / (self.fuel_consumption * 250)
        return ratio
    def __add__(self, other):
        total_cargo_weight = self.cargo_weight + other.cargo_weight
        return Truck(tank_capacity=self.tank_capacity,
                     fuel_consumption=self.fuel_consumption,
                     average_speed=self.average_speed,
                     cargo_weight=total_cargo_weight)

class Bus(Car):
    def __init__(self, tank_capacity, fuel_consumption, average_speed, passengers_count):
        super().__init__(tank_capacity, fuel_consumption, average_speed)
        self.passengers_count = passengers_count

    def calculate_ratio(self):
        ratio = self.passengers_count / (self.fuel_consumption * 250)
        return ratio

    def __add__(self, other):
        total_passengers_count = self.passengers_count + other.passengers_count
        return Bus(tank_capacity=self.tank_capacity,
                   fuel_consumption=self.fuel_consumption,
                   average_speed=self.average_speed,
                   passengers_count=total_passengers_count)

# Sample of usage 1
truck_one = Truck(tank_capacity=100, fuel_consumption=10, average_speed=60, cargo_weight=5000)
bus_one= Bus(tank_capacity=80, fuel_consumption=8, average_speed=50, passengers_count=30)

print(f"The truck will cover {truck_one.calculate_distance():.2f} km before running out of fuel.")
print(f"The weight-to-fuel ratio for the truck over 250 km is: {truck_one.calculate_ratio():.2f}")

print(f"The bus will cover {bus_one.calculate_distance():.2f} km before running out of fuel.")
print(f"The passenger-to-fuel ratio for the bus over 250 km is: {bus_one.calculate_ratio():.2f}")





#Sample of usage 2:
truck_two = Truck(tank_capacity=600, fuel_consumption=20, average_speed=120, cargo_weight=3000)
bus_two= Bus(tank_capacity=10, fuel_consumption=81, average_speed=210, passengers_count=40)
print(f"The truck will cover {truck_two.calculate_distance():.2f} km before running out of fuel.")
print(f"The weight-to-fuel ratio for the truck over 250 km is: {truck_two.calculate_ratio():.2f}")

print(f"The bus will cover {bus_two.calculate_distance():.2f} km before running out of fuel.")
print(f"The passenger-to-fuel ratio for the bus over 250 km is: {bus_two.calculate_ratio():.2f}")


total_truck = truck_one + truck_two
print("Sum of cargo weigth:", total_truck.cargo_weight)

total_bus = bus_one + bus_two
print("Sum of bus passengers:", total_bus.passengers_count)
