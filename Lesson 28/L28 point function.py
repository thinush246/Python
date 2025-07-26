class Point:
    def __init__(self, x=0, y=0):  # Corrected constructor
        self.x = x
        self.y = y

    # Method to print points in coordinate format
    def __str__(self):  # Corrected __str__ method
        return "({0}, {1})".format(self.x, self.y)

# Create Object
p1 = Point(2, 3)
print(p1)