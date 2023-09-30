from itertools import combinations

def count_team_divisions(N, M, pairs):
    
    # 頂点の組み合わせから可能なチームの組み合わせを生成する
    teams_combinations = combinations(range(1, N+1), M)

    count = 0
    for teams in teams_combinations:
        print(teams)
        valid = True
        for a, b in pairs:
            a_team = next((i for i, team in enumerate(teams, start=1) if a in team), None)
            b_team = next((i for i, team in enumerate(teams, start=1) if b in team), None)
            if a_team and b_team and a_team == b_team:
                valid = False
                break
        if valid:
            count += 1

    return count

# 使用例
N, T, M = [int(x) for x in input().split()]
pairs = []
for _ in range(M):
    tmp = [int(x) for x in input().split()]
    pairs.append((tmp[0], tmp[1]))

if M > T:
    print(0)
else:
    print(count_team_divisions(N, M, pairs))