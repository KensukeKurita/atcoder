
N = int(input())
S = input()

past = set()
now = (0, 0)
past.add(now)
for s in S:
    if s == "R":
        new = (now[0] + 1, now[1])
    elif s == "L":
        new = (now[0] - 1, now[1])
    elif s == "U":
        new = (now[0], now[1] + 1)
    else:
        new = (now[0], now[1] - 1 )

    if new in past:
        print("Yes")
        break
    past.add(new)
    now = new
else:
    print("No")