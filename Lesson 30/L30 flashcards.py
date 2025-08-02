class flashcard:
    def __init__(self, w, m):
        self.word = w
        self.meaning = m

    def __str__(self):
        # we will return a string
        return self.word + ' ( ' + self.meaning + ' )'

flash = []
print("Welcome to flashcard application")

# the following loop will be repeated until
# user stops adding flashcards
while True:
    word = input("Enter the word you want to add to flashcard: ")
    meaning = input("Enter the meaning of the word: ")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0 if you want to add another flashcard, otherwise enter 1: "))

    if option:
        break

print()
# printing all the flashcards
print("Your flashcards:")
for i in flash:
    print(">", i)