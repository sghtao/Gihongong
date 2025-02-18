n = int(input())
c = 0
p = 0
b = 0
cnt = 0
for i in range(n):
    cnt += 1
    if cnt % 12 == 0:
        b += 1
    elif cnt % 3 == 0:
        p += 1
    elif cnt % 2 == 0:
        c += 1
    
print(c, p, b)