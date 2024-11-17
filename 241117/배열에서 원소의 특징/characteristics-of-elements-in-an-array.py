arr = list(map(int, input().split()))

arr1 = []

for i in arr:
    if i % 3 != 0:
        arr1.append(i)
    else:
        break

print(arr1[-1])