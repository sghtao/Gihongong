a = input().split("-")
a[1], a[2] = a[2], a[1]

print(f"010-{a[1]}-{a[2]}")