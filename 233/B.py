
L, R = map(int, input().split())
S = input()

l = S[0:L-1]
c = S[L-1:R]
r = S[R: len(S)]

print(l + c[::-1] + r)
