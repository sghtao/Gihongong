n = int(input())

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end = "")
    
    for j in range(1 + 2*i):
        print("*", end = "")
    print()
    

for i in range(n-1):
    for j in range(i+1):
        print(" ", end = "")
    for j in range(2*n - 3 - 2*i):
        print("*", end = "")
    print()