import numpy as np


def main():

    N = int(input())
    h_list = [int(h) for h in input().split()]

    dp = np.zeros(N, dtype=int)
    dp[1] = np.abs(h_list[1] - h_list[0])
    for i in range(2, N):
        way1 = dp[i-2] + np.abs(h_list[i] - h_list[i-2])
        way2 = dp[i-1] + np.abs(h_list[i] - h_list[i-1])
        if way1 < way2:
            dp[i] = way1
        else:
            dp[i] = way2

    print(dp[-1])

main()