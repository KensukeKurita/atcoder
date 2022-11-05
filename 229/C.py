# coding : utf-8
import sys
import copy


def main():

    # DPで解く。
    # DP[i番目のチーズ][重さ] =　最大のおいしさ
    # DP[i][j] = max(DP[i-1][j], DP[i-1][j-1]+(Ai*1), DP[i-1][j-2]+(Ai*2), ..., DP[i-1][j-Bi]+(Ai*Bi))
    inf = -10**9
    max_weight = W
    dp = [inf for _ in range(max_weight+1)]
    dp[0] = 0

    for delicious, weight in Cheese:
        old_dp = copy.deepcopy(dp)
        for j in range(max_weight+1):
            ww = min(j, weight)
            dp[j] = max([old_dp[j-b] + b*delicious for b in range(0, ww+1)])

    for dd in reversed(dp):
        if dd >= 0:
            print(dd)
            return


if __name__ == "__main__":
    input = sys.stdin.readline
    N, W = map(int, input().split())
    Cheese = [[int(i) for i in input().split()] for _ in range(N)]
    main()