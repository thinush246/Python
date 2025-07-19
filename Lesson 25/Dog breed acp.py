class Dog:
    # Class variable
    animal = "Dog"
    
    def __init__(self, breed, colour):
        # Instance variables
        self.breed = breed
        self.colour = colour
    
    def display(self):
        print(f"Animal: {Dog.animal}")
        print(f"Breed: {self.breed}")
        print(f"Colour: {self.colour}")
        print()

# Create two different dog objects
dog1 = Dog("Labrador", "Yellow")
dog2 = Dog("German Shepherd", "Black and Brown")

# Display details of both dogs
dog1.display()
dog2.display()
