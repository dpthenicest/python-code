# simple sorting - Bubble Sort Implementation

arr = [2, 3, 1, 5, 1]

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubble_sort(arr))

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

print(f"Selection sort: {selection_sort(arr)}")


# Merge Sort
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
    return array


print(f"Merge sort: {merge_sort(arr)}")a

import random

arr1 = random.choices(range(1, 100), k=10)
print(arr1)
print(bubble_sort(arr1))


# for i in range(len(arr)):
#   for j in range(i + 1, len(arr)):
#     if arr[j] < arr [i]:
#       temp = arr[i]
#       arr[i] = arr[j]
#       arr[j] = temp
#     else:
#       continue

for i in arr:
    print(i)

# make this a list comprehension
squared = [x**2 for x in arr]
print(squared)

print()

a = 10
b = 7
a, b = b, a
print(a, b)