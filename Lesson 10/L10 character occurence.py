#Take input of a word
#string = input("Please enter your own word or sentence : ")
string = "My name is thinush"

#take input of a character
#char = input("Please enter your own character")
char = "h"

i = 0
count = 0

#loop will find the occurence of character
while(i < len(string)): #string operation
    if(string[i] == char): #check each letter of the word wheather it's the same as the character we want to find
        count = count + 1

    i = i + 1 #increase the i value until reach the length of the word. i is the position of each letter in the word

#Display the result
print(f"The total Number {char} character has occurred = {count} times")