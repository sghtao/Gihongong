a, b = map(int, input().split())

divisor = 10**21

q = a // b
d = a % b

result = str(q)+"."

for i in range(20):
    r *= 10
    d = r // b
    result += str(d)
    remainder %= b

