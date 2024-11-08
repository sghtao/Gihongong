arr = input().split()

a = int(arr[0])
b = int(arr[1])

sum_var = 0

for i in range(a, b+1):
    sum_var += i

print(sum_var)