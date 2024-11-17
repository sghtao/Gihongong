arr = list(map(int, input().split()))

arr1 = arr[::2]
arr2 = arr[1::2]

if sum(arr1) > sum(arr2):
    print(sum(arr1) - sum(arr2))
else:
    print(sum(arr2)-sum(arr1))