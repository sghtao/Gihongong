n = int(input())

for i in range(2, n+1):
    약수 = 0
    for j in range(2, i):
        if i % j == 0:
            약수 += 1
    
    if 약수 == 0 :
        print(i, end = " ")
