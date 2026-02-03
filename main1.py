# import math

# name = "beau"

# print(type(name) == str)
# print(isinstance(name, str))

# age = 30
# currency = 19.99

# print(type(currency))
# print(isinstance(currency, float))

# rounded = 5 // 2
# print(rounded)

# # MATH module functions
# print(math.ceil(4.2))
# print(math.floor(4.7))
# print(math.sqrt(16))
# print(math.pow(3, 3))
# print(math.pi)
# print(math.fabs(-7))
# print(math.factorial(5))
# print(math.log10(1000))
# print(math.sin(math.pi / 2))
# print(math.cos(0))
# print(math.tan(math.pi / 4))

# Boolean
# cond1 = True
# cond2 = False

# print(not cond1)
# print(cond1 and cond2)
# print(cond1 or cond2)

# tenerary operator
# def is_adult(age):
#   return True if age > 18 else False

# print(is_adult(20))

from xml.etree.ElementPath import find


name = "beau"
name += " is my name."
name = name.title()
print(name)
print(name.islower())

print(""" 
Beau is learning Python!
""")


print(name.isalpha())
print(name.startswith("B"))
print(len(name))
print("au" in name)
print(name.index("B"))
print(name.replace("beau", "me"))
print(name*3)
print(name.strip())
print(name.split(" "))
print("\n")
print(name.join(["My", "name", "is", "also", "jonny"]))


def is_sentence_alphabetic(sentence):
  words = sentence.split(" ")
  for word in words:
    if not word.isalpha():
      return False
  return True

print(is_sentence_alphabetic(name))
print(name)
print(name.find("Name"))

n_name = 'Be\'au'
print(n_name)

print("name" is "name1")

print(name[1:-4])

# Boolean

done = None

if done:
  print('yes')
else:
  print('no')

book_1_read = True
book_2_read = False

is_book_read = any([book_1_read, book_2_read])
print(f"Is any book read? {is_book_read}")

are_all_books_read = all([book_1_read, book_2_read])
print(f"Are all books read? {are_all_books_read}")

# Complex Numbers
num1 = 2 +3j
num2 = complex(2,3)

print(num1.real, num2.imag)
print(round(5.49, 0))

from enum import Enum

class State(Enum):
  START = 1
  RUNNING = 2
  STOPPED = 3

print(State.RUNNING.value)
print(type(State.START))
print(list(State))
print(len(State))

# age = input("What is your age? ")
# print("Your age is: " + age)


# Control Statements

condition = True
name = "Rager"

if condition == True:
  print("The condition")
  print("was True")
elif name == "Roger":
  print("Hello Roger!")
elif name == "Syd":
  print("Hello Syd!")
elif name == "Flavio":
  print("Hello Flavio!")
else:
  print("The condition")
  print("was False")

# lists

dogs = ["Roger", 1, "Syd", True]

dogs[2] = "Beau"
new_dogs = dogs.copy()

print(dogs[2])
print(new_dogs)

del new_dogs

greeting = "Hello, World!"
print(greeting)

del greeting

print(len(dogs))

dogs.append("Judah")
print(dogs)

dogs.extend(["Flavio", "Max"])
print(dogs)

dogs += ["Don", "Scooby"]
print(dogs)

if "drink" not in dogs:
  print("No drink found")

dogs.remove("Judah")
print(dogs)

print(dogs.pop())
print(dogs)

dogs.insert(2, "Test")
print(dogs)

dogs1 = dogs[:4]
print(dogs1)

dogs[1:1] = ["New1", "New2"]
print(dogs)

dogs.remove(dogs[3])
dogs.remove(dogs[5])
print(sorted(dogs, key=str.lower))
print(dogs)

print(f"deleted an item in a list: {dogs.pop(1)}")
print(dogs)

dogs2 = dogs[:]

# Tuples

names = ("Roger", "Syd", "Beau")
names[0]
names.index("Syd")
len(names)

print("Roger" in names)
names[0:2]

print(sorted(names))

new_tuple = names + ("Flavio", "Max")
print(new_tuple)

# dictionaries

dict_dog = {
  "name": "Roger",
  "age": 8,
  "color": "brown"
}

# dict_dog["name"] = "Syd"
print(dict_dog["name"])
print(dict_dog.get("name"))
print(dict_dog.get("color", "brown"))

print(dict_dog.keys())
print(dict_dog.values())
print(list(dict_dog.values()))
print(list(dict_dog.keys()))

print(dict_dog.items())
print(list(dict_dog.items()))

print(len(dict_dog))

print("age" in dict_dog.keys())
print(dict_dog.popitem())

if "age" in dict_dog:
  del dict_dog["age"]
print(dict_dog)

# Reverse List
# Palindrom