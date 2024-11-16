arr = list(map(int, input().split()))
new_arr = []

for i in arr:
    if i != 0:
        new_arr.append(i)
    else:
        break


cnt = 0
sum_var = 0
for i in new_arr:
    if i % 2 ==0:
        sum_var += i
        cnt += 1


print(cnt, sum_var)