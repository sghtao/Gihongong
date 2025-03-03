n = int(input())
sum_val = 0


for i in range(n):
    a = int(input())
    sum_val += a

print(sum_val, end = " ")
print(f"{sum_val / n:.1}")