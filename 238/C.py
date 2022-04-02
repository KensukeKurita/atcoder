
def sum_diff(a, l):
    n = l - a + 1

    A_L_mod = a + l
    n_mod = n

    return (n_mod * A_L_mod) //2


def n_digit_sum(n):
    min_ = 10**(n-1)
    max_ = 10**n - 1

    n = max_ - min_ + 1
    # print(f"項数は{n}")

    return (n*(min_+max_) // 2) + ((-1)*min_*n + 1*n)


MOD = 998244353
# MOD = 10

N = int(input())
keta = len(str(N))
print(N*N)
ans = 0
for i in range(1, keta):
    ans += int(n_digit_sum(i)) % MOD
    # ans += sum_diff(10**(i-1), 10**i-1)

ans += sum_diff(1, N-10**(keta-1)+1) % MOD
# print(n_digit_sum(1))
# print(n_digit_sum(2))
# print(sum([a for a in range(1, 90+1)]))
print(ans)
