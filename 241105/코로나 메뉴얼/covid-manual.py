arr1 = input().split()
arr2 = input().split()
arr3 = input().split()


counter = 0
if arr1[0] == "Y" and int(arr1[1]) >= 37:
    counter += 1

if arr2[0] == "Y" and int(arr2[1]) >= 37:
    counter += 1

if arr3[0] == "Y" and int(arr3[1]) >= 37:
    counter += 1


if counter >= 2:
    print("E")
else:
    print("N")