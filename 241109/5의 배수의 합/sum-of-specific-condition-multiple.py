arr = input().split()

a = int(arr[0])
b = int(arr[1])
sum_var = 0

if a < b:
    for i in range(a, b+1):
        if i % 5 == 0:
            sum_var += i
elif a > b:
    for i in range(b, a+1):
        if i % 5 == 0:
            sum_var += i
else:
    if a % 5 == 0:
        print(a)

print(sum_var)