import itertools
import math
def com(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
N, M = map(int, input().split())
couple = set()
for i in range(M):
    aux = [int(a) for a in input().split()]
    k = aux[0]
    x = aux[1::]
    for a, b in itertools.combinations(x, 2):
        couple.add((a,b))
    
if len(couple) == com(N, 2):
    print("Yes")
else:
    print("No")