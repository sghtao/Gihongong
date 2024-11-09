확인기 = True
for i in range(5):
    a = int(input())
    if a % 3 != 0:
        확인기 = False


if 확인기 == True:
    print(1)
else:
    print(0)