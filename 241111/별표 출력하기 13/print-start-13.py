n = int(input())

for i in range(2*n):
    if i % 2 != 0:
        for j in range((i+1)//2):
            print("*", end = " ")
        print()
    else:
        for j in range(n - i//2):
            print("*", end = " ")
        print()