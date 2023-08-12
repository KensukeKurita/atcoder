def best():

    N = int(input())
    A = [int(a) for a in input().split()]

    orange = 0
    for l in range(N):
        for r in range(l + 1, N + 1):
            eat = (r - l) * min(A[l:r])
            if eat >= orange:
                orange = eat

    print(orange)


if __name__ == "__main__":
    best()
