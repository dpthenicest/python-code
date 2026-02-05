# functions

def hello(name, age):
  print(f'Hello, {name}! You are {str(age)}.')

hello("Syd", 20)
hello("Quincy", 30)
hello("User", 25)


def change(value):
  value["name"] = "Syd"

val = {"name": "Beau"}
change(val)
print(val)


def hello1(name):
  if not name:
    return
  print('Hello, ' + name + '!')

hello1("Roger")

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
  
print(factorial(5))

class Animal:
  def walk(self):
    print("Walking... " + self.name)

class Dog(Animal):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def bark(self):
    print("Woof!") 

dog1 = Dog("Chelsea", 5)
dog1.bark()

dog1.walk()

print(type(dog1))


# lambda functions

add = lambda num : num * 2
print(add(5))
multiply = lambda x, y : x / y
print(int(multiply(10, 2)))

# map(), filter(), reduce()

numbers = [1, 2, 3, 4, 5]

double = lambda a: a * 2

result = map(lambda a: a * 2, numbers)
print(list(result))


result=filter(lambda n: n%2==0,numbers)
print(list(result))

from functools import reduce

expenses = [
  ('Dinner', 80),
  ('Car Repair', 120),
]

sum = reduce(lambda a, b: a + b, numbers)
print(sum)

sum1 = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum1)

arr_mat = [
  [1, 2, 3],
  [2, 5, 3],
  [4, 1, 7]
]

print(len(arr_mat))

