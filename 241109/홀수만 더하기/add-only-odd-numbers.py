n = int(input())
sum_var = 0
for i in range(n):
    a = int(input())
    if (a % 2 != 0) and (a % 3 == 0):
        sum_var += a

print(sum_var)