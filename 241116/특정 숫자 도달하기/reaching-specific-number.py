arr = list(map(int, input().split()))

new_arr = []

for i in arr:
    if i < 250:
        new_arr.append(i)
    else:
        break

sum_var = 0

for i in new_arr:
    sum_var += i

print(sum_var, f"{sum_var/len(new_arr):.1f}")