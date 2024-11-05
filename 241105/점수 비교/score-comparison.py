arr1 = input().split()
arr2 = input().split()

Am = int(arr1[0])
Ae = int(arr1[1])

Bm = int(arr2[0])
Be = int(arr2[1])

if Am > Bm and Ae > Be:
    print(1)
else:
    print(0)