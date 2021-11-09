# coding : utf-8
import sys

def main(s, t):

    dp =[[int(0) for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[-1][-1])

    # ここから文字列を復元する
    return

if __name__ == "__main__":
    input = sys.stdin.readline

    s = str(input())
    t = str(input())
    main(s, t)