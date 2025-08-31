
# 方向の移動量
directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

Rt, Ct, Ra, Ca = map(int, input().split())
N, M, L = map(int, input().split())

S = []
for _ in range(M):
    s, a = input().split()
    S.append((s, int(a)))

T = []
for _ in range(L):
    t, b = input().split()
    T.append((t, int(b)))


def solve():
    """
    Nが大きくて１つの移動を追うことはできない。
    MやLは小さいのでそのまとまった移動を１単位として追うとよさそう。
    
    (U,10)と(R,20)なら、(U,10)(R,10)と分解。
    この１単位では同じ方向に進むので、2回以上会うことはない(0回か1回)。
    """
    # 初期相対位置
    rel_r = Rt - Ra
    rel_c = Ct - Ca
    
    count = 0
    step = 0
    
    s_idx = 0
    t_idx = 0
    s_pos = 0  # S内での現在位置
    t_pos = 0  # T内での現在位置
    
    while step < N:
        # 現在のセグメントでの文字
        s_char = S[s_idx][0]
        t_char = T[t_idx][0]
        
        # 現在のセグメントで残っているステップ数
        s_remaining = S[s_idx][1] - s_pos
        t_remaining = T[t_idx][1] - t_pos
        
        # このイテレーションで処理するステップ数
        process_steps = min(s_remaining, t_remaining, N - step)
        
        # 相対移動量（1ステップあたり）
        dr_s, dc_s = directions[s_char]
        dr_t, dc_t = directions[t_char]
        rel_dr = dr_s - dr_t # 下方向への相対運動量
        rel_dc = dc_s - dc_t # 右方向への相対運動量
        
        # 相対移動が(0,0)の場合、同じ位置でスタートしていれば全部カウントされる。
        if rel_dr == 0 and rel_dc == 0:
            if rel_r == 0 and rel_c == 0:
                count += process_steps
        else:
            # rel_r + t * rel_dr = 0 かつ rel_c + t * rel_dc = 0 を満たすtが存在すれば1カウント
            
            # 一方向だけの移動の場合
            if rel_dr == 0:
                if rel_r == 0 and rel_dc != 0:
                    # rel_c + t * rel_dc = 0 => t = -rel_c / rel_dc
                    if rel_c % rel_dc == 0:
                        t = -rel_c // rel_dc
                        if 1 <= t <= process_steps:
                            count += 1
            elif rel_dc == 0:
                if rel_c == 0 and rel_dr != 0:
                    # rel_r + t * rel_dr = 0 => t = -rel_r / rel_dr
                    if rel_r % rel_dr == 0:
                        t = -rel_r // rel_dr
                        if 1 <= t <= process_steps:
                            count += 1
            else:
                # 両方向移動の場合
                # rel_r + t * rel_dr = 0 => t = -rel_r / rel_dr
                # rel_c + t * rel_dc = 0 => t = -rel_c / rel_dc
                # 両方を満たすtが存在するか確認
                if rel_dr != 0 and rel_dc != 0:
                    if rel_r % rel_dr == 0 and rel_c % rel_dc == 0:
                        t1 = -rel_r // rel_dr
                        t2 = -rel_c // rel_dc
                        if t1 == t2 and 1 <= t1 <= process_steps:
                            count += 1
        
        # 現在の位置を更新。相対移動かけるステップ数
        rel_r += rel_dr * process_steps
        rel_c += rel_dc * process_steps
        step += process_steps
        
        # インデックスを更新
        s_pos += process_steps
        t_pos += process_steps
        
        if s_pos == S[s_idx][1]:
            s_idx = (s_idx + 1) % M
            s_pos = 0
        
        if t_pos == T[t_idx][1]:
            t_idx = (t_idx + 1) % L
            t_pos = 0
    return count

print(solve())