class SriLanka():
    def capital(self):
        print("Colombo is the capital of Sri Lanka.")

    def language(self):
        print("Sinhala is the national language of Sri Lanka.")

    def type(self):
        print("Sri Lanka is a developing country.")

# Class 2
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

# Object Creation
obj_sl = SriLanka()
obj_usa = USA()

# Common Interface
for country in (obj_sl, obj_usa):
    country.capital()
    country.language()
    country.type()
    print()