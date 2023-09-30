N, H, X = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]

for i, p in enumerate(P):
    if p >= (X-H):
        print(i+1)
        break