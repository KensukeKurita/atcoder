# coding : utf-8
import numpy as np

def main():
    N, M = map(int, input().split())
    list_A = np.array([int(a) for a in input().split()])
    list_B = np.array([int(b) for b in input().split()])

    result = 10**9
    for i in range(N):
        va = np.full_like(list_B, list_A[i])
        vc = np.abs(va - list_B)
        m = np.min(vc)
        if m < result:
            result = m

    print(result)

def main2():
    N, M = map(int, input().split())
    A = [int(a) for a in input().split()]
    B = [int(b) for b in input().split()]
    A.sort()
    B.sort()
    print(A)
    print(B)

    for i in range(N-1):
        a = A[i]
        b = B[i]
        


        
main2()
# main()