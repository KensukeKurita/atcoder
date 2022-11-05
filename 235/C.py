
def c(list_a, x, k):
    count = list_a.count(x)
    if k > count:
        return -1
    else:
        return count


N, Q = map(int, input().split())
A = [int(a) for a in input().split()]

for i in range(Q):
    x, k = map(int, input().split())
    count = c(A, x, k)
    if count == -1:
        print(-1)
    else:
        ans = 0
        for i in range(N):
            if A[i] == x:
                ans += 1

            if ans == k:
                print(i+1)
                break
