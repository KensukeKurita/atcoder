
S1 = input()
S2 = input()

total = S1 + S2
black = total.count("#")

if black >= 3:
    print("Yes")
else:
    if S1[0] == "#" and S2[1] == "#":
        print("No")
    elif S1[1] == "#" and S2[0] == "#":
        print("No")
    else:
        print("Yes")
