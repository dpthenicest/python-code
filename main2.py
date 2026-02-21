num = []

n_arr = [ 1, 4, 5, 2, 7, 4, 2, 6, 3, 0, 4, 5, 6, 7, 9, 10, 4, 17, 12, 11, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

for i in range(len(n_arr)):
    if(n_arr[i] % 4 == 0):
        num.append(1)
    elif(n_arr[i] % 3 == 0):
        num.append(2)
    else:
        num.append(3)


print(num)

n_sum = [0] * 10

for i in range(len(num)):
    if num[i] == 1:
        n_sum[0] += 1
    elif num[i] == 2:
        n_sum[1] += 1
    else:        
        n_sum[2] += 1

print(n_sum)

n_sum.remove(0)
sum_arr = []

for i in range(len(n_sum)):
    if n_sum[i] > 0:
        sum_arr.append(n_sum[i])

print(sum_arr)

r = 4
w = 2
x = 1

rwx = r | w | x

print(rwx)

if (rwx & r) == r:
    print("Read permission is granted.")

print(bin(rwx))
print(bin(r))
print(bin(w))
print(bin(x))

arr_2d = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    print(arr_2d[i])


