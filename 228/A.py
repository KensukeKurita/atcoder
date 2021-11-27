S, T, X = map(int, input().split())

if S < T:
    if X >= S and X < T:
        print("Yes")
    else:
        print("No")
else:
    # S ~ 24 and 0 ~ T
    if X >= S:
        print("Yes")
    elif X < T:
        print("Yes")
    else:
        print("No")