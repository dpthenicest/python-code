# String data type

# literal assignment
first = "Fortune"
last = "Precious"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?

I was just checking in.
                          All good?
'''

print(multiline)

# Escaping special characters
sentence = 'I\'m back \tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first.title())

print(multiline.title())
print(multiline.replace("good", "ok"))

print(len(multiline))
multiline += "                          "
multiline = "              " + multiline
print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(10))
print("Muffin".ljust(16, ".") + "$2".rjust(10))
print("CheeseCake".ljust(16, ".") + "$4".rjust(10))

# String index values
print(first[1])
print(first[-1])
print(first[:])

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("e"))
print(first.count("o"))

# Boolean data type
myvalue = True