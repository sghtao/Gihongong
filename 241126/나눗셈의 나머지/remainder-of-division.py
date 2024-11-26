arr = list(map(int, input().split()))

a, b = arr[0], arr[1]


arr1 = [0] * 10

while True:
    if a <= 1:
        break
    c = a % b
    arr1[c] += 1
    a //= b
  

sum_var = 0

for i in arr1:
    sum_var += (i ** 2)

print(sum_var)

