users = ['dave', 'john', 'sara']

data = ['dave', 42, True]

emptylist = []

print("dave" in emptylist)

print(users[0])
print(users[-1])
print(users[-2])

print(users.index('sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

# Add items
users.append('elsa')
print(users)

users += ['jason']
print(users)

users.extend(['robert', 'james'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'bob')
print(users)

users[2:2] = ['eddie', 'alex']
print(users)

users[1:3] = ['robert', 'jpj']
print(users)

# remove items
users.remove('bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
# print(data)

data.clear() # clears and empties a list
print(data)

users[1:2] = ['Dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples

mytuple = tuple(('dave', 42, True))

anothertuple = (1, 4, 2, 8, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('neil')
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
