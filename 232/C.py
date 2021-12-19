import itertools


def main():
    N, M = map(int, input().split())

    T_A = {}
    T_B = {}
    for i in range(1, N+1):
        T_A[str(i)] = set()
        T_B[str(i)] = set()

    for i in range(M):
        a, b = map(int, input().split())
        T_A[str(a)].add(b)
        T_A[str(b)].add(a)

    for i in range(M):
        c, d = map(int, input().split())
        T_B[str(c)].add(d)
        T_B[str(d)].add(c)

    for P in list(itertools.permutations(list(range(1, N+1)))):
        T_new = {}
        for i in range(1, N+1):
            b_list = []
            for b in list(T_B[str(i)]):
                b_list.append(P[b-1])

            T_new[str(P[i-1])] = set(b_list)

        if T_A == T_new:
            print("Yes")
            return

    print("No")
    return


if __name__ == "__main__":
    main()

