n = int(input())

arr = list(map(int, input().split()))
new_arr = []

for i in arr:
    if i  == 0:
        print(0)
        break
    elif i % 2 == 0:
        new_arr.append(i)
    

for i in new_arr[::-1]:
    print(i, end = " ")


