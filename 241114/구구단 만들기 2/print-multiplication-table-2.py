arr = input().split()

a, b = int(arr[0]), int(arr[1])


for i in range(4):
    for j in range(b-a+1):
        print(f"{b-j} * {2*(i+1)} = {(b-j)*(2*(i+1))}", end = " ")
        if j < b-a:
            print("/", end = " ")
    print()