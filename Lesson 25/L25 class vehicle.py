class Vehicle:
    # create init method or constructor
    def __init__(self,speed,mile):
        # bind the arguments
        self.max_speed = speed
        self.mileage = mile

#object creation
bike = Vehicle(240, 18) #object 1
car = Vehicle(700, 30) #object 2

#access the variables inside init method
print("Bike Max Speed:",bike.max_speed)
print("Bike Mileage:",bike.mileage)

print()

#access the variables inside init method#access the variables inside init method
print("Car Max Speed:",car.max_speed)
print("Car Mileage:",car.mileage)
