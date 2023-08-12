N = int(input())
A = [int(a) for a in input().split()]

odd = []
even = []
for a in A:
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)

even.sort()
odd.sort()

if len(odd) >= 2 and len(even) >= 2:
    e = even[-1] + even[-2]
    o = odd[-1] + odd[-2]
    if e >= o:
        print(e)
    else:
        print(o)
elif len(odd) <= 1 and len(even) >=2:
    print(even[-1] + even[-2])
elif len(odd) >= 2 and len(even) <= 1:
    print(odd[-1] + odd[-2])
else:
    print(-1)
