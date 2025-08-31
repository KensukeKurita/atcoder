import itertools
import time

def check(s: str) -> bool:
    # 文字列SをK文字ずつに分割する
    for i in range(0, len(s)-K+1):
        part_s = s[i:i+K]
        # 知っているものはパス
        if part_s in rotated_parts:
            return True
        elif part_s in not_rotated_parts:
            continue
        
        # 文字種の数で判定
        kinds = len(set(part_s))
        if kinds == 1:
            return True
        elif kinds > K // 2 + 1:
            continue

        if check_rotate(part_s):
            rotated_parts.add(part_s)
            return True
        else:
            not_rotated_parts.add(part_s)
    else:
        return False

def check_rotate(ss: str) -> bool:
    if K % 2 == 0:
        # Kが偶数の場合
        h1 = ss[:K//2]
        # 逆順
        h2 = ss[K//2:][::-1]
        return h1 == h2
    else:
        # Kが奇数の場合
        h1 = ss[:K//2]
        # 逆順
        h2 = ss[K//2+1:][::-1]
        return h1 == h2


N, K = map(int, input().split())
S = input()

# 回文になっている部分文字列も保存しておく
rotated_parts = set()
not_rotated_parts = set()

# 文字列Sを並び替える
# 文字列Sを並び替えて得られる文字列を全パターンをset()に保存する
done = set()
permutations = set()
for perm in itertools.permutations(S):
    s = ''.join(perm)
    if s in done:
        continue
    # すでに同じ文字列が存在する場合はスキップ
    if s in permutations:
        continue
    if check(s):
        continue
    else:
        permutations.add(s)
    done.add(s)
        

print(len(permutations))