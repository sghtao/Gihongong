arr = input().split()

a, b = int(arr[0]), int(arr[1])

comp = 0
for i in range(a, b+1):
    sum_var = 0
    for j in range(1, i):
        if i % j == 0:
            sum_var += j
        
    if sum_var == i:
        comp += 1
        
    
print(comp)