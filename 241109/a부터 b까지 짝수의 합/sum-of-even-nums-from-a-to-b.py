arr = input().split()

a, b = int(arr[0]), int(arr[1])
sum_var = 0
for i in range(a, b+1):
    if i % 2 == 0:
        sum_var += i

print(sum_var)