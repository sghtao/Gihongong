n = int(input())


for i in range(n):
    for j in range(n-i):
        print(f"{i+1} * {j+1} = {(i+1)*(j+1)}", end = " ")
        
        if j < n-i-1:
            print("/", end = " ")
    print()