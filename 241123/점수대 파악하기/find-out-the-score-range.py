arr = list(map(int, input().split()))

arr1 = [0] * 10

for i in arr:
    if i == 0:
        break
    elif i < 10:
        pass
    else:
        n = i // 10
        arr1[n-1] += 1

arr1 = arr1[::-1]

for i in range(1, 11):
    cnt = arr1[i-1]
    print(f"{10 * (11 - i)} - {cnt}")