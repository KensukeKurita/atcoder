# coding : utf-8
import math
import numpy as np

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    N = int(input())
    C = np.array([int(c) for c in input().split()])

    m = np.max(C)
    max_list = []
    for i in range(m, 0, -1):
        max_list.append(np.count_nonzero(C >= i))

    print(max_list)
    mainasu = 0
    for i in range(1, m+1):
        aaa = max_list[i-1]
        print("{} is {} ".format(m-i+1, aaa), end="")
        test = 0
        for j in range(2, aaa+1):
            test += comb(aaa, j)
        print(test)
        
    
    print(np.prod(C) - mainasu)

def test():
    N = int(input())
    C = np.array([int(c) for c in input().split()])
    
    ng = 0
    for i in range(N):
        for j in range(1, C[i-1]):
            


test()
# main()