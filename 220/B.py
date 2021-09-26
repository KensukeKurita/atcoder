
def n(X, n):

    X = str(X)

    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out

K = int(input())
A, B = [int(a) for a in input().split()]

print(n(A, K) * n(B, K))
