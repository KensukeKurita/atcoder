import numpy as np

def main():
    N = int(input())

    a, b, c = [], [], []
    for i in range(N):
        aa, bb, cc = map(int, input().split())
        a.append(aa)
        b.append(bb)
        c.append(cc)

    # i日目にX(X=A,B,C)の活動をしたときのi日目の幸福度をdp[i, X]としておく。
    dp = np.zeros((N, 3), dtype=int)
    dp[0, 0] = a[0]
    dp[0, 1] = b[0]
    dp[0, 2] = c[0]

    for i in range(N-1):

        # 0をする
        if dp[i, 1] > dp[i, 2]:
            dp[i+1, 0] = dp[i, 1] + a[i+1]
        else:
            dp[i+1, 0] = dp[i, 2] + a[i+1]

        # 1をする
        if dp[i, 0] > dp[i, 2]:
            dp[i+1, 1] = dp[i, 0] + b[i+1]
        else:
            dp[i+1, 1] = dp[i, 2] + b[i+1]

        # 2をする
        if dp[i, 0] > dp[i, 1]:
            dp[i+1, 2] = dp[i, 0] + c[i+1]
        else:
            dp[i+1, 2] = dp[i, 1] + c[i+1]

    print(int(dp[N-1].max()))


if __name__ == '__main__':
    main()