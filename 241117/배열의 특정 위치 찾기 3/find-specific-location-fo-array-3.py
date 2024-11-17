arr = list(map(int, input().split()))

new_arr = []

for i in arr:
    if i != 0:
        new_arr.append(i)
    else:
        break

sum_var = new_arr[-1] + new_arr[-2] + new_arr[-3]

print(sum_var)