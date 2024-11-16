arr = list(map(int, input().split()))
new_arr = []
for i in arr:
    if i != 0:
        new_arr.append(i)
    else:
        break


print(sum(new_arr), f"{sum(new_arr) / len(new_arr):.1f}")