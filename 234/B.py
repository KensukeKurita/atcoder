
import itertools
import math

def r(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]- p2[1])**2)

N = int(input())
p = []
for _ in range(N):
    xx, yy = map(int, input().split())
    p.append([xx, yy])

length = []
for a, b in itertools.combinations(p, 2):
    length.append(r(a, b))

print(max(length))

