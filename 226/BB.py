# coding : utf-8

def main():

    # 配列を文字列として扱い、setで同じものを除外.
    N = int(input())
    A = []
    for i in range(N):
        aux = str(input()).replace(" ", "")
        l = int(aux[0])
        a = aux[1:len(aux)]
        A.append(a)

    B = set(A)
    print(len(B))

    return


def main2():

    import numpy as np
    # 長さごとにグループ化
    N = int(input())
    A = {}
    for i in range(N):
        aux = [int(a) for a in input().split()]
        l = aux[0]
        a = aux[1:len(aux)]
        if not str(l) in A.keys():
            A[str(l)] = []

        isAdd = True
        for r in A[str(l)]:
            if a == r:
                isAdd = False
                break

        if isAdd:
            A[str(l)].append(a)

    count = 0
    for key in A.keys():
        count += len(A[key])
    print(count)


if __name__ == "__main__":
    main2()
