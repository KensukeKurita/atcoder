
alpha = "abcdefghijklmnopqrstuvwxyz"
S = str(input())
T = str(input())

s0 = alpha.find(str(S[0]))
t0 = alpha.find(str(T[0]))

d = t0 - s0

S_new = ""
for i in range(len(S)):
    n = (alpha.find(S[i]) + d) % 26
    S_new += alpha[n]

if S_new == T:
    print("Yes")
else:
    print("No")

