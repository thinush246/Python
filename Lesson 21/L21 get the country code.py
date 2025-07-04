country_code = {'India': '0091',
            'Australia': '0025',
            'Sri lanka': '0094'}

# search dictionary for country code of Sri lanka
print("Country code for Sri lanka -")
print(country_code.get('Sri lanka', 'Not Found'))

print()

# search dictionary for country code of Japan
print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))