squared = lambda num : num * num

print(squared(2))

addTwo = lambda num : num + 2

print(addTwo(12))

sum = lambda a, b : a + b

print(sum(2, 5))

# # # # # # # # # # 
def func_builder(x):
  return lambda num : num + x

addTen = func_builder(10)
addTwenty = func_builder(20)

print(addTen(7))
print(addTwenty(7))

# # # # # # # # # 

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))

# # # # # # # # # # # # # # # # 

lambda num : num % 2 != 0