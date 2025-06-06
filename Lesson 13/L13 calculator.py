def add(P, Q):
    return P + Q #sending or returning the result

def subtract(P, Q):
    return P - Q

def multiply(P, Q):
    return P * Q

def divide(P, Q):
    return P / Q

print("Please select operation")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

#choise = input("Please enter choise (a/b/c/d): ")
choise = 'b'
#num_1 = int(input("Please enter the first number"))
num_1 = 6
#num_2 = int(input("Please enter the second number"))
num_2 = 4
print()

if choise.lower() == 'a': #covert input into lowercase and then check if it's 'a' letter
    result = add(num_1, num_2)
    print(num_1, "+", num_2, "=", result)

elif choise.lower() == 'b':
    result = subtract(num_1, num_2)
    print(num_1, "-", num_2, "=", result)

elif choise.lower() == 'c':
    result = multiply(num_1, num_2)
    print(num_1, "*", num_2, "=", result)

elif choise.lower() == 'd':
    result = divide(num_1, num_2)
    print(num_1, "/", num_2, "=", result)

else:
    print("This is an invalid input")