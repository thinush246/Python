# Assigning Different Variables
name = "Penguin"
age = 15
is_student = True
weight = 38.5

# Printing Different Variables and their Data Type
print("original:")
print("Name:", name)
print("Data Type of Name is", type(name))

print("Age:", age)
print("Data Type of Age is", type(age))

print("is_student :", is_student)
print("Data Type of is_student is", type(is_student))

print("Weight:", weight)
print("Data Type of weight is", type(weight))

print()
print()

#Type casting to convert the datatype of variables
print("After Type Casting....")
age = str(age)
print("age after typecasting: ",age)
print("Data Type of age is", type(age))

weight = int(weight)
print("weight after typecasting: ",weight)
print("Data Type of weight is",type(weight))