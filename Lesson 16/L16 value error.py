try :
    #num = int(input("Enter a number : "))
    num = int("fg")
    print("the number entered is: ",num)

except NameError as e: #using NameError
    print("Exception: ",e)

except ValueError as ve: #using ValueError
    print("Exception: ",ve)

print("I am outside the try-except block")#always excuted and displayed the message
print()