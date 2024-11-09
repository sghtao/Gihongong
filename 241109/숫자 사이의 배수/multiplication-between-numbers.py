arr = input().split()

a = int(arr[0])
b = int(arr[1])
sum_var = 0
cnt = 0 
for i in range(a , b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_var += i
        cnt += 1

print(sum_var, f"{sum_var/cnt:.1f}")