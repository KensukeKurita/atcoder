import numpy as np


def main():
    N, K = map(int, input().split())
    h = [int(hh) for hh in input().split()]

    dp = np.full(N, 10**10, dtype=int)
    dp[0] = 0
    for i in range(1, N):
        # 足場i に来る方法は、i-K, ..., i-1から飛んでくる
        if i-K > 0:
            min_from = i-K
        else:
            min_from = 0

        for j in range(min_from, i):
            cost = dp[j] + np.abs(h[i] - h[j])
            if cost < dp[i]:
                dp[i] = cost

    print(int(dp[-1]))

main()