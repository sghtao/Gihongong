n = int(input())

arr = list(map(float, input().split()))

aver_grade = sum(arr) / n
print(f"{aver_grade:.1f}")
if aver_grade >= 4.0:
    print("Perfect")
elif aver_grade >= 3.0:
    print("Good")
else:
    print("Poor")