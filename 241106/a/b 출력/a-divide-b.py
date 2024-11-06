arr = input().split()

a = int(arr[0])
b = int(arr[1])


print(a/b, end = "")

for i in range(19):
    print(((a%b))//b, end = "")