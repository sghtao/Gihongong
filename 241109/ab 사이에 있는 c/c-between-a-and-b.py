arr = input().split()

a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
cnt = 0
for i in range(a, b+1):
    if i % c == 0:
        print("YES")
        break
    else:
        cnt += 1
        continue
if cnt == b - a + 1:
    print("NO")