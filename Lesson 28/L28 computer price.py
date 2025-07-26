class Computer:
    def __init__(self):  # constructor
        self.__maxprice = 900  # private variable

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):  # FIXED: Added colon here
        self.__maxprice = price

# create object
c = Computer()

print("Original price:")
c.sell()
print()

# trying to change it directly
print("After trying to change it directly")
c._maxprice = 1000  # This creates a new variable, doesn't change the private one
c.sell()
print()

# using setter function
print("Change it using setMaxPrice method")
c.setMaxPrice(1500)
c.sell()