
N = int(input())
S = input()


def count_swaps_to_pattern(s, pattern):
    """文字列sを指定されたパターンに変換するのに必要な隣接交換回数を計算"""
    # Aの文字だけ考えればいい。
    asis_A_pos = []
    tobe_A_pos = []

    swaps = 0

    for i in range(len(s)):
        if s[i] == 'A':
            asis_A_pos.append(i)
        if pattern[i] == 'A':
            tobe_A_pos.append(i)

    for i in range(len(tobe_A_pos)):
        # i番目のAをtobeの位置に移動するのに必要な交換回数は、現在位置と目標位置の差
        swaps += abs(tobe_A_pos[i] - asis_A_pos[i])
        asis_A_pos[i] = tobe_A_pos[i]  # 移動後の位置に更新

    return swaps

# 両パターンへの変換に必要な操作回数を計算
swaps1 = count_swaps_to_pattern(S, "AB" * N)
swaps2 = count_swaps_to_pattern(S, "BA" * N)

# 最小値を出力
print(min(swaps1, swaps2))
