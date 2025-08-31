import math

def is_infected(N, coordinates, D):
    infected = [False] * N 
    infected[0] = True 
    old_list = set()
    old_list.add(0)
    new_list = set()

    # 感染の伝搬を繰り返す
    changed = True
    while changed:
        changed = False
        for i in old_list:
            for j in range(N):
                if not infected[j]:
                    distance = math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
                    if distance <= D:
                        infected[j] = True
                        new_list.add(j)
                        changed = True 
        old_list = new_list
        new_list = set()

    return infected

N, D = map(int, input().split())

position = []
for i in range(N):
    tmp = input().split()
    position.append([int(tmp[0]), int(tmp[1])])

result = is_infected(N, position, D)
for i, status in enumerate(result):
    if status:
        print("Yes")
    else:
        print("No")