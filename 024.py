import numpy as np

N, K = map(int, input().split())
A = np.array([int(a) for a in input().split()])
B = np.array([int(b) for b in input().split()])
C = A - B 
k = np.sum(np.abs(C))
if k <= K and (K-k) % 2 == 0:
    print("Yes")
else:
    print("No")
