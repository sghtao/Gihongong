cnt = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(f"{i} * {j} = {i*j}", end = " ")
        
    
        if cnt == 171:
            print("", end = " ")
        elif cnt % 2 != 0:
            print("/", end = " ")
        else:
            print()
        
        
        cnt += 1