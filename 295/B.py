R, C = map(int, input().split())
B = []
for r in range(R):
    B.append([])
    tmp = input()
    for b in tmp:
        B[r].append(b)

for r in range(R):
    for c in range(C):
        b = B[r][c]
        if b == ".":
            pass
        elif b == "#":
            pass
        else:
            B[r][c] = "."
            bomb = int(b)

            for r_ in range(R):
                for c_ in range(C):
                    length = abs(r-r_) + abs(c-c_)
                    if length <= bomb and B[r_][c_] == "#":
                        B[r_][c_] = "."

# output
for r in range(R):
    for c in range(C):
        print(B[r][c], end="")
    print()