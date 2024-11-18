arr = list(map(int, input().split()))

arr1 = []
for i in arr:
    if i != 0:
        if i % 2 != 0:
            i += 3
            arr1.append(i)
        else:
            i //= 2
            arr1.append(i)


for i in arr1:
    print(i, end = " ")
    
