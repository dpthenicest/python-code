arr = [4, 5, 3, 5, 2, 1, 2, 5, 6, 3, 0, 4, 5, 6, 7, 9, 10, 4,
       17, 12, 11, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

s_arr = merge_sort(arr)

def binary_search(arr, target):
    low = 0
    high= len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if  target == arr[mid]:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None

target_index = binary_search(s_arr, 5)

print(f"Target index: {target_index}")

def find_all_occurences(arr, target_index):
    val = arr[target_index]
    index = target_index
    indices = [index]
    print(f"target index: {target_index}, value: {val}")
    while index > 0 and arr[index - 1] == val:
        index -= 1
        indices.append(index)

    index = target_index
    while index < len(arr) - 1 and arr[index + 1] == val:
        index += 1
        indices.append(index)
    
    return indices


print(f"All occurences of target value: {s_arr[11]} -  {find_all_occurences(s_arr, target_index)}")

def palindrom(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True