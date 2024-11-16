n = int(input())
num_pass = 0
num_fail = 0

for i in range(n):
    arr = list(map(int, input().split()))
    if (sum(arr) / 4) >= 60:
        print("pass")
        num_pass += 1
    else:
        print("fail")
        num_fail += 1


print(num_pass)

 
