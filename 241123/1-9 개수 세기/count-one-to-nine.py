n = int(input())
arr = list(map(int, input().split()))
arr1 = [0] * 9

for i in arr:
    arr1[i-1] += 1



for i in arr1:
    print(i)
    