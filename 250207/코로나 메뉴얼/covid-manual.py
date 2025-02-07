arr = input().split()
arr1 = input().split()
arr2 = input().split()
cnt = 0

at, bt, ct = int(arr[1]) , int(arr1[1]), int(arr2[1])

if arr[0] == "Y" and at >= 37:
    cnt += 1
if arr1[0] == "Y" and bt >= 37:
    cnt += 1
if arr2[0] == "Y" and ct >= 37:
    cnt += 1

if cnt >= 2:
    print("E")
else:
    print("N")