m = int(input())

if m == 2:
    print(28)
elif (m < 8 and m % 2 != 0) or (m >= 8 and m % 2 == 0):
    print(31)
else:
    print(30)