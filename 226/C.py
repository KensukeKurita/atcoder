# coding : utf-8
import numpy as np


def main():

    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        aux = [int(a) for a in input().split()]
        T.append(aux[0])
        K.append(aux[1])
        A.append(aux[2:len(aux)])

    dp = np.full((N), 10**10, dtype="uint64")
    dp[0] = T[0]
    for i in range(1, N):
        cost = T[i]
        for j in range(K[i]):
            cost += dp[A[i][j] - 1]

        if cost < dp[i]:
            dp[i] = cost

    print(dp[-1])


if __name__ == "__main__":
    main()
