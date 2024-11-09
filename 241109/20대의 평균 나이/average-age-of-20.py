sum_var = 0
cnt = 0
while True:
    n = int(input())
    if 20 <= n <= 29:
        sum_var += n
        cnt += 1
    else:
        print(f"{sum_var/cnt:.2f}")
        break