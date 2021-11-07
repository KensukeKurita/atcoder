import numpy as np


def main():
    D = 998244353
    N = int(input())
    A = [int(a) for a in input().split()]

    dp = np.zeros((N, 10))
    for j in range(10):
        if j == A[0]:
            dp[0, j] = 1
        else:
            dp[0, j] = 0

    print(dp.shape)
    for i in range(N-1):
        for j in range(10):
            dp[i+1, (j + A[i+1]) % 10] += dp[i, j]
            dp[i+1, (j * A[i+1]) % 10] += dp[i, j]

    for j in range(10):
        print("{}".format( int(dp[N-1][j])) )

main()