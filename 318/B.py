N = int(input())

sheets = []
for _ in range(N):
    a, b, c, d = [int(x) for x in input().split()]
    sheets.append({"x": (a, b), "y": (c, d)})

S = 0
for x in range(0, 100):
    for y in range(0, 100):
        X = x + 0.5
        Y = y + 0.5
        for sheet in sheets:
            if (sheet["x"][0] < X < sheet["x"][1]) and (sheet["y"][0] < Y < sheet["y"][1]):
                S += 1
                break

print(S)