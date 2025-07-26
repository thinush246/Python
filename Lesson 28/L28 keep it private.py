class myClass:
    # private variable
    __privateVar = 27

    # private method
    def __privMeth(self):
        print("I'm inside class myClass")

    # function to print value of private variable
    def hello(self):
        print("Private Variable value",myClass.__privateVar)

# object creation and method call
foo = myClass()
foo.hello()
foo.__privMeth #this will give error, cz private can't be accessed