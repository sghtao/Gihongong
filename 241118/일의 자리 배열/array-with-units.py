arr = input().split()

a, b = int(arr[0]), int(arr[1])

arr1 = [a, b]

for i in range(3, 11):
    n = arr1[-1] + arr1[-2]
    if n >= 10:
        n -= 10
        arr1.append(n)
    else:
        arr1.append(n)


for i in arr1:
    print(i, end = " ")
