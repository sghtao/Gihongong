word = ["L", "E", "B", "R", "O", "S"]

idx = -1

w = input()

for i in range(len(word)):
    if word[i] == w:
        idx = i

if idx == -1:
    print("None")
else:
    print(idx)