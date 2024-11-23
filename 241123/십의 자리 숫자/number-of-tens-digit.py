arr = list(map(int, input().split()))
arr1 = [0] * 9

for i in arr:
    if i == 0:
        break
    elif i < 10:
        pass
    else:
        n = i // 10
        arr1[n-1] += 1


for i in range(1, 10):
    cnt = arr1[i-1]
    print(f"{i} - {cnt}")
