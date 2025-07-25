class Person( object ): #parent class
    # __init__ is known as the constructor
    def __init__(self, nm, idno):
        self.name = nm
        self.idnumber = idno

    def display(self):
        print(self.name)
        print(self.idnumber)

class Employee(Person): # child class
    def __init__(self, name, idnumber, wage, position):
        self.salary = wage
        self.post = position

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

# creation of an object variable or an instance
a = Employee('Jessica', 626012, 500000, "permanent employee")

# calling a method of class person using its instance
a.display()