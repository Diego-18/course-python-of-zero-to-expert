country = 'colombia'
currency = 'COP'

capital = '''Its capital is:
Bogota '''

print(country)
print(currency)
print(capital)

# Type of variables
print(type(country))
print(type(currency))


# Accessing to the elements of a string
print(country[0])
print(country[1])
print(country[2])
print(country[3])
print(country[4])
print(country[5])
print(country[6])
print(country[7])

print('-----------------')

# Accessing to the elements of a string in reverse
print(country[-1])
print(country[-2])
print(country[-3])
print(country[-4])
print(country[-5])
print(country[-6])
print(country[-7])
print(country[-8])

# Concatenation
print('The currency in ' + country + ' is: ' + currency)

# Length of a string
print('The word ' + country + ' has a total number of letters: ')
print(len(country))

# Methods
print(country.count('o'))               # Count the number of times a character appears in a string
print(country.upper())                  # Convert all characters to uppercase
print(country.lower())                  # Convert all characters to lowercase
print(country.capitalize())             # Convert the first character to uppercase
print(country.title())                  # Convert the first character of each word to uppercase
print(country.swapcase())               # Convert uppercase characters to lowercase and vice versa
print(country.replace('o', 'a'))        # Replace a character with another
print(country.split('o'))               # Split the string into a list of strings
print(country.strip())                  # Remove spaces at the beginning and end of the string
print(country.lstrip())                 # Remove spaces at the beginning of the string
print(country.rstrip())                 # Remove spaces at the end of the string
print(country.find('o'))                # Find the position of a character in a string
print(country.index('o'))               # Find the position of a character in a string
print(eval('2 + 2'))                    # Evaluate an expression
exec('print("Hello Dev")')                  # Execute a string as Python code