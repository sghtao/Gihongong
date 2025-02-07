am, ae = map(int, input().split())
bm, be = map(int, input().split())

if am > bm:
    print("A")
elif bm > am:
    print("B")
elif ae > be:  # am == bm 인 경우 ae와 be를 비교
    print("A")
else:  # am == bm 이고 ae <= be 인 경우
    print("B")