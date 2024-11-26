
cnt = [0] * 4

for i in range(3):
    arr = input().split()
    temp = int(arr[1])
    if arr[0] == "Y":
        if temp >= 37:
            cnt[0] += 1
        else:
            cnt[2] += 1
    else:
        if temp >= 37:
            cnt[1] += 1
        else:
            cnt[3] += 1
        
    

for i in cnt:
    print(i, end = " ")
if cnt[0] >= 2:
    print("E")
    


