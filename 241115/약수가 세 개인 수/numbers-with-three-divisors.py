arr = input().split()

a, b = int(arr[0]), int(arr[1])
cnt = 0

for i in range(a, b+1):
    약수 = 0
    for j in range(1, i+1):
        if i % j == 0:
            약수 += 1
    if 약수 == 3:
        cnt += 1

print(cnt)