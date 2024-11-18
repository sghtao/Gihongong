n = int(input())

arr = list(map(int, input().split()))

arr1 = []

for i in arr:
    if i % 2 == 0:
        arr1.append(i)


for i in arr1:
    print(i, end = " ")