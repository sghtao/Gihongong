n = int(input())
나누는수 = 1
cnt = 0
while n > 1:
    n //= 나누는수
    나누는수 += 1
    cnt += 1

print(cnt)