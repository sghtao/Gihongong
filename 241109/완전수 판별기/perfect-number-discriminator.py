n = int(input())
sum_var = 0

for i in range(1, n):
    if n % i == 0:
        sum_var += i

print("P") if sum_var == n else print("N")