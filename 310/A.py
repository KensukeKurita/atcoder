N, P, Q = [int(x) for x in input().split()]
D = min([int(x) for x in input().split()])

print(min(P, Q+D))