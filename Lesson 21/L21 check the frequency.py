test_dict = {'Codingal' : 2,
            'is': 2,
            'best': 2,
            'for': 2,
            'Coding': 1
            }

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize value
v = 2

# Using loop
# Selective key values in dictionary
count = 0

for key in test_dict:
    if test_dict[key] == v:
        count = count + 1

# printing result
print(f"Frequency of {v} is: " + str(count))