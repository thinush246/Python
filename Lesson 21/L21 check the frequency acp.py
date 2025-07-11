test_dict = {'Codingal': 2,
             'is': 2,
             'best': 2,
             'for': 2,
             'Coding': 1
            }

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize value
v = 1  # Changed from 2 to 1

# Using loop to count frequency
count = 0
for key in test_dict:
    if test_dict[key] == v:
        count += 1

# printing result
print(f"Frequency of {v} is: " + str(count))
