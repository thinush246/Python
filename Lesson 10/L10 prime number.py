#take two input from the user
#lower = int(input("Enter a lower range: "))
lower = 5
#upper = int(input("Enter a upper range: "))
upper = 31

print()
print("Prime numbers between",lower,"and",upper,"are: ")

#display the result
for num in range(lower, upper + 1):
    if num > 1: # all prime numbers are greater than 1
        for i in range(2, num):
            if (num % i) == 0: # if the number can be divided by other number, then it's not prime number so we need to stop checking
                break
        else:
            print(num)