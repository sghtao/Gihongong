sum_var = 0
cnt = 0

for i in range(10):
    n = int(input())
    if 0 <= n <= 200:
        sum_var += n
        cnt += 1

print(sum_var, f"{sum_var/cnt:.1f}")