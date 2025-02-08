a, b = map(int, input().split())

divisor = 10**21

q = a // b
d = a % b

result = str(q)+"."

for i in range(20):
    d *= 10
    n = d // b
    result += str(n)
    d %= b

print(result)