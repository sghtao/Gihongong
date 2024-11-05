arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
elif a < c < b or b < c < a:
    print(c)