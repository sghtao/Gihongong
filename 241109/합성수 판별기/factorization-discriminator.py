n = int(input())
합성수니 = False
for i in range(2, n):
    if n % i == 0:
        합성수니 = True

    
if 합성수니 == True:
    print("C")
else:
    print("N")