
def binary_search(arr, target):
  low = 0
  high = len(arr) - 1

  while low <= high:
    mid = (low + high) // 2
    if target == arr[mid]:
      return mid
    elif target > arr[mid]:
      low = mid + 1
    else:
      high = mid - 1
  return None

arr = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(arr, 2))

def binary_search_recursive(arr, target, low, high):
  if low > high:
    return None

  mid = (low + high) // 2
  if target == arr[mid]:
    return mid
  elif target > arr[mid]:
    return binary_search_recursive(arr, target, mid + 1, high)
  else:
    return binary_search_recursive(arr, target, low, mid - 1)
  

# what is the diffference between the two binary search functions?
# The first function, `binary_search`, is an iterative implementation of the binary search algorithm. It uses a while loop to repeatedly divide the search interval in half until the target value is found or the search interval is empty.
# The second function, `binary_search_recursive`, is a recursive implementation of the binary search algorithm. It calls itself with updated low and high indices to narrow down the search interval until the target value is found or the search interval is empty. The recursive version may be more elegant and easier to understand for some, but it can also lead to stack overflow errors if the input array is too large.

# check for issues in this code:

def bin_search(arr, x):
        low = 0
        high = len(arr) - 1
        count = 0
        
        while low <= high:
            mid = (low + high) // 2
            if x == arr[mid]:
                count += 1
            elif x > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return count

print(bin_search(arr, 2))
# The issue with this code is that it does not correctly count the occurrences of the target value in the array. The function only checks for the target value at the midpoint of the search interval, and if it finds a match, it increments the count. However, it does not continue to search for additional occurrences of the target value in the left and right halves of the array. As a result, if there are multiple occurrences of the target value, the function will only count one of them. To fix this issue, the function should be modified to continue searching for the target value in both halves of the array after finding a match at the midpoint.

def bin_search(arr, x):
        low = 0
        high = len(arr) - 1
        count = 0
        
        while low <= high:
            mid = (low + high) // 2
            if x == arr[mid]:
                count += 1
                # Search for additional occurrences in the left half
                left_index = mid - 1
                while left_index >= low and arr[left_index] == x:
                    count += 1
                    left_index -= 1
                
                # Search for additional occurrences in the right half
                right_index = mid + 1
                while right_index <= high and arr[right_index] == x:
                    count += 1
                    right_index += 1
                
                break  # Exit the loop after counting all occurrences
            elif x > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return count

# how many times wil


# should i use linear search or binary search for this problem?
# The choice between linear search and binary search depends on the characteristics of the data you are working with.

# the data is sorted in ascending order, which should I use?
# If the data is sorted in ascending order, you should use binary search. Binary search is much more efficient than linear search for sorted data, as it has a time complexity of O(log n) compared to O(n) for linear search. Binary search works by repeatedly dividing the search interval in