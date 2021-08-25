

def main():
    N = int(input())

    # グラフの初期化
    city = {}
    for i in range(1, N+1):
        city[str(i)] = []

    # グラフの作成
    for i in range(N-1):
        a, b = map(int, input().split())
        city[str(a)].append(b)
        city[str(b)].append(a)

    done = []
    now = 1
    nowth = 0
    flag = True
    i = 0
    while flag:
        done.append(now)

        # 今の街につながっている都市のうち行っていないのは？
        undone_now = []
        for c_city in city[str(now)]:
            if not c_city in done:
                undone_now.append(c_city)
            

        if len(undone_now) == 0:
            if now == 1:
                flag = False
            else:
                nowth += -1
                now = done[nowth]
        else :
            undone_now.sort()
            now = undone_now[0]
            nowth += 1


    print(*done)

    return 

main()