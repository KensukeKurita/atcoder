def get(l):
    a = l[0]
    b = l[1:N]

    # bのなかからaの次に小さい値を探す.
    for bb in sorted(b, reverse=True):
        if bb < a:
            break
    b.remove(bb)
    b.append(a)
    return bb, b

N = int(input())
P = list(int(x) for x in input().split())

for i in range(N-2, -1, -1):
    sonomama = P[0:i]
    target = P[i:N]
    if sorted(target) == target:
        continue
    else:
        s1 , s2 = get(target)
        sonomama.append(s1)
        sonomama.extend(sorted(s2, reverse=True))
        break

print(*sonomama)
"""
1回入れ替え
3 1 7 4 2
3 1 7 2 4

3 7 4 2 1
3 7 4 1 2

---------------
2回入れ替え
3 4 7 1 2
3 4 [7] (1 2) 自分(2)よりもでかい数を見つける. それよりも小さい部分がもっと小さくなるか？
3 4 2 (1 7) カッコないをでかい順に
3 4 2 7 1

3 7 1 2 4
3 4 (1 2 7) カッコないをでかい順に
3 4 7 2 1 

3 7 2 1 4
3 [7] (2 1 4)
1 2 4, 1 4 2

3 7 1 2 4

9 8 6 5 10 3 1 2 4 7
9 8 6 5 10 3 1 2 (4 7) ()内は降順
9 8 6 5 10 3 1 (2 4 7) ()内は降順
9 8 6 5 10 3 (1 2 4 7) ()内は降順
9 8 6 5 10 (3 1 2 4 7) ()内は降順じゃない
(3 1 2 4 7)の次に小さいものを探す.
2 (1 3 4 7) 3の次に小さい数と入れ替えて, ()を昇順に並べる.
2 (7 4 3 1)



"""