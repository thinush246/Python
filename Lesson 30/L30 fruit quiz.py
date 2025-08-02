import random
class FruitQuiz:  # Added colon here
    # create a constructor
    def __init__(self):
        # Create a dictionary of fruits as keys and color as value
        self.fruits = {'apple': 'red',
                       'grape': 'purple',
                       'watermelon': 'green',
                       'banana': 'yellow'}  # Removed extra space

    # Function for the quiz, here a fruit will be chosen randomly
    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))

            print(f"What is the color of {fruit}")
            user_answer = input()

            if (user_answer.lower() == color):
                print("Correct answer")
            else:
                print("Wrong answer")

            option = int(input("enter 0 , if you want to play again otherwise enter 1: "))
            if (option):
                break

print("welcome to fruit quiz ")
fq = FruitQuiz()
fq.quiz()