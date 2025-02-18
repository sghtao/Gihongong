arr = input().split()

C = arr[0]
N = int(arr[1])
n = 0

if C == "A":
    for i in range(N):
        n += 1
        print(n, end = " ")
elif C == "D":
    for i in range(N):
        print(N, end = " ")
        N -= 1
        