S = input()

if "a" in S:
    j = 1
    i = 1
    for a in S:
        if a == "a":
            j = i
        i += 1
    print(j)
else:
    print(-1)


















