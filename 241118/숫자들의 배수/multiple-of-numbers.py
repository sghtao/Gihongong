n = int(input())
cnt = 0
arr = []
i = 1
while cnt < 2:
    new_n = n * i
    arr.append(new_n)
    i += 1
    if new_n % 5 == 0:
        cnt += 1



for i in arr:
    print(i, end = " ")