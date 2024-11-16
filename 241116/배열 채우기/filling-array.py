arr = list(map(int, input().split()))
new_arr = []
for i in arr:
    if i != 0:
        new_arr.append(i)
    else:
        break


for i in new_arr[::-1]:
    print(i, end = " ")
