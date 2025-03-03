N = int(input())
sum_val = 0

for i in range(N):
    n = int(input())
    if n % 2 != 0 and n % 3 == 0:
        sum_val += n

print(sum_val)