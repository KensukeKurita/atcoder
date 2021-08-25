# coding : utf-8

from abc import abstractproperty


def main():
    N, M = map(int, input().split())
    city = {}
    for i in range(1, N+1):
        city[str(i)] = []

    for i in range(M):
        a, b = map(int, input().split())
        city[str(a)].append(b)
        city[str(b)].append(a)
    
    city_depth = {}
    Q = [1]
    depth = 0
    while (len(Q) >= 1):
        new_Q = []
        for q in Q:
            city[str(q)] = depth
            for child in city[str(q)]:
                if not str(child) in city_depth:
                    new_Q.append(child)

        Q = new_Q
        depth += 1

main()