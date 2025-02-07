arr = input().split()
arr1 = input().split()

aa = int(arr[0])
ba = int(arr1[0])

if aa >= 19 and arr[1] == "M" or ba >= 19 and arr1[1] == "M":
    print(1)
else:
    print(0)