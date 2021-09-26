
def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    X = int(input())

    sum_A = sum(A)
    dvi = X // sum_A

    now = sum_A * dvi
    if now > X:
        k = N * dvi
        print(k)
        return

    for i in range(N):
        now += A[i]
        if now > X:
            k = N * dvi + (i+1)
            break

    print(k)
    return


main()