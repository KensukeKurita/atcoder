
def main():
    N, M = map(int, input().split())

    P = []
    C = []
    F = {}
    for i in range(N):
        text = [int(x) for x in input().split()]
        P.append(text[0])
        C.append(text[1])
        F[str(i)] = set(text[2::])

    end_set = set()

    for i in range(N):
        for j in range(N):
            if i == j or (i, j) in end_set:
                continue
            if check(P, C, F, i, j):
                print("Yes")
                return
            end_set.add((i, j))
    else:
        print("No")


def check(P, C, F, i, j):

    if P[i] >= P[j] and F[str(i)] <= F[str(j)]:        
        if P[i] > P[j]:
            return True
        for Fj in F[str(j)]:
            if Fj not in F[str(i)]:
                return True
    else:
        return False

if __name__ == "__main__":
    main()
