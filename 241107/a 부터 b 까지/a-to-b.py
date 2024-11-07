arr = input().split()

a = int(arr[0])
b = int(arr[1])
print(a, end = " ")

while a < b:
    if a % 2 != 0:
        a *= 2
    else:
        a += 3
    
    if a <= b:
        print(a, end = " ")