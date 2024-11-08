n = int(input())

for i in range(1, n+1):
    ni = str(i)
    if ("3" in ni) or ("6" in ni) or ("9" in ni):
        print(0, end = " ")
    else:
        print(i, end = " ")