#Input a number
#num = int(input("Enter the number: "))
num = 6789
print()

t = num
numLen = 0

#iterate the loop
while t>0:
    numLen = numLen+1
    t = int(t/10)

if numLen >= 4:
    numLen = int(numLen/2)
    chk = 0

    while num > 0: #iterate loop
        rem = num%10

        if chk--numLen:
            midOne = rem
        elif chk==(numLen-1):
            midTwo = rem

        num = int(num/10)
        chk = chk+1

    prod = midOne * midTwo #Products of middle digits

    #display the result
    print(f"Products of Mid digits ({midOne} * {midTwo}) = {prod}")

else:
    print("It's not a 4 or more than 4-digit number! ")