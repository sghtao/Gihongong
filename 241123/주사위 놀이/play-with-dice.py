arr = list(map(int, input().split()))


arr1 = [0] * 6

for i in arr:
    arr1[i-1] += 1


for i in range(1, 7):
    cnt = arr1[i-1]
    print(f"{i} - {cnt}")