n = int(input())

for i in range(n):
    nn = int(input())
    if nn % 2 != 0 and nn % 3 == 0:
        print(nn)