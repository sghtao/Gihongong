arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
확인기 = False

for i in range(a, b+1):
    if i % c == 0:
        확인기 = True

if 확인기 == True:
    print("NO")
else:
    print("YES")