classroom = 0
corridor = 0
restroom  = 0
cnt = 0
n = int(input())

for i in range(n):
    if i == 0:
        pass
    elif i % 12 == 0:
        restroom += 1
    elif i % 12 != 0 and i % 6 == 0:
        corridor += 1
    elif i % 3 == 0:
        corridor += 1
    elif i % 2 == 0:
        classroom += 1
    

print(classroom, corridor, restroom)