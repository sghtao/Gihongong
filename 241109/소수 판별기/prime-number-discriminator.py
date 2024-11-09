n = int(input())
소수니 = True

for i in range(2, n):
    if n % i == 0:
        소수니 = False

if 소수니 == True:
    print("P")
else:
    print("C")