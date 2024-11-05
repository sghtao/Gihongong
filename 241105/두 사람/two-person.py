arr1 = input().split()
arr2 = input().split()

fa = int(arr1[0])
fs = arr1[1]

sa = int(arr2[0])
ss = arr2[1]

if (fa >= 19 and fs == "M") or (sa >= 19 and ss == "M"):
    print(1)
else:
    print(0)