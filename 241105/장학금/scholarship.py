arr = input().split()

mid = int(arr[0])
final = int(arr[1])

if mid < 90:
    print(0)
elif final < 90:
    print(0)
elif final < 95:
    print(50000)
else:
    print(100000)