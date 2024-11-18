arr = list(map(int, input().split()))

a, b = arr[0], arr[1]
arr1 = [a, b]


for i in range(3, 11):
    n = arr1[-1] + (2 * arr1[-2])
    arr1.append(n)

for i in arr1:
    print(i, end = " ")